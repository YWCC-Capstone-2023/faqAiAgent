import os, json, pandas as pd
from platform import system

from discord.ext import commands
import discord

from neuralintents import GenericAssistant

class Ask(commands.Cog):
    """Cog for /ask command on FaqAiBot
    """
    SPREADSHEET = "https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"
    PATH_TO_INTENTS = ''
    PATH_TO_MODEL = ''

    def __init__(self, bot) -> None:
        self.bot = bot
        print("Ask Loaded\n")

        self.__train_agent()



    def __path_creator(self) -> None:
        """
        Change paths based on which system cog is running on
        """
        userSystem = system()

        self.PATH_TO_INTENTS = os.getcwd() + "\\intents\\" if userSystem == 'Windows' else os.getcwd() + "/intents/"
        self.PATH_TO_MODEL = os.getcwd() + "\\trained_model\\" if userSystem == 'Windows' else os.getcwd() + "/trained_model/"



    @commands.hybrid_command(name='ask', description="Ask the bot a question!", guild_ids=[1072948383955816459])
    async def ask(self, interaction: discord.Interaction, question:str) -> None:
        """Ask the Bot a question
        """
        response = self.agent.request(question)
        await interaction.reply(f"Hi, {interaction.author.mention}! {response}", ephemeral=True)



    @ask.error
    async def ask_error(self, ctx:commands.Context, error:Exception) -> None:
        if isinstance(error, commands.errors.MissingRole):
            await ctx.reply(f"You do not have permission to do that!", ephemeral=True)
        else:
            await ctx.reply(f"Sorry {ctx.author.mention},I do not understand! Please ping the Professor!", ephemeral=True)
    


    def __convert_col_to_list(self, df:pd.DataFrame, col_name:str, new_col_name:str = "") -> pd.DataFrame:
        """
        Converts every row of a column in a pandas DataFrame into a list containing
        strings delimited by a semi-colon.
        
        Args:
        -----------
            df (pandas.DataFrame): The DataFrame containing the column to be converted.
            col_name (str): The name of the column to be converted.
            new_col_name (str): The new name of the column to be converted. Defaults to original name
        
        Returns:
            pandas.DataFrame: A new DataFrame with the converted column.
        """
        if new_col_name == "": new_col_name = col_name
        
        df[new_col_name] = df[col_name].apply(lambda x: str(x).strip().split(";"))
        
        return df
    


    def __load_spreadsheet_as_intents(self,df:pd.DataFrame, new_filename:str = PATH_TO_INTENTS) -> None:
        """
        Writes to a file a DataFrame as a json object

        Args:
        -----------
            df (pandas.DataFrame) : The dataframe to be written to the file
            new_filename (str) : The name of the file, Default = intents.json
        """
        self.__path_creator()

        df = self.__convert_col_to_list(df, "patterns")
        df = self.__convert_col_to_list(df, "responses")

        res_df = pd.DataFrame().assign(tag = df["tag"], patterns = df['patterns'], responses = df['responses'], context_set = "")

        json_df = res_df.to_json(orient = "table", index = False)

        parsed_df = json.loads(json_df)

        json_obj = json.dumps(parsed_df, indent = 4)


        with open(os.path.join(self.PATH_TO_INTENTS,'intents.json'), 'w') as f:
            f.write(json_obj)

        with open(os.path.join(self.PATH_TO_INTENTS,'intents.json'), 'r') as f:
            obj = json.load(f)

        intents = obj['data']

        res = {"intents" : intents}

        with open(os.path.join(os.getcwd(), self.PATH_TO_INTENTS, 'intents.json'), 'w') as f:
            f.write(json.dumps(res, indent=4))



    def __get_intents(self, url:str, new_filename:str = 'intents.json') -> None:
        """
            Will generate new intents file from specified spreadsheet url

            Args:
            -----------
                url (str): url containing the spreadsheet to load
                new_filename (srt): name of intents file, Default = intents.json
        """

        df = pd.read_csv(url)

        self.__load_spreadsheet_as_intents(df, new_filename=new_filename)



    def __train_agent(self) -> None:
        """
        Train AI agent
        
        """
        
        self.__get_intents(self.SPREADSHEET)

        self.agent = GenericAssistant(os.path.join(os.getcwd(), self.PATH_TO_INTENTS, 'intents.json'), model_name='faqAiAgent')

        #check if there already exists some presaved model, speed up the bot login
        #implement method to check for last modified date here
    
        self.agent.train_model()
        self.agent.save_model(model_name= os.path.join(self.PATH_TO_MODEL, f'{self.agent.model_name}'))



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Ask(bot))