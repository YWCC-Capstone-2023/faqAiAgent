import logging , os, pandas as pd

from discord.ext import commands
import discord

import pygsheets

# setup access to spreadsheet
path_to_creds = os.path.join(os.getcwd(), 'credentials', 'service_account_credentials.json')

if os.path.exists(path_to_creds):
    gc = pygsheets.authorize(service_file=path_to_creds)

else: logging.log(msg='Failed to Load Service Account Credentials for spreasheet')

sh = gc.open('Question and Answers_new').sheet1

class AddModal(discord.ui.Modal, title = "Add a Question and Answer"):
    question = discord.ui.TextInput(
        label = 'Question', 
        required=True, 
        placeholder="Input Question Here",
        style=discord.TextStyle.paragraph
    )

    answer = discord.ui.TextInput(
        label = 'Answer', 
        required=True, 
        placeholder="Input Answer Here",
        style=discord.TextStyle.paragraph
    )
    
    tag = discord.ui.TextInput(
        label = 'Tag',
        placeholder="Input TagHere",
        style=discord.TextStyle.short,
        default="default_tag"
    )
    

    """on_submit -> return all of the modal text inputs
    """
    async def on_submit(self, interaction: discord.Interaction, /) -> None:
        
        q = self.question
        a = self.answer
        t = self.tag

        add_to_spreadsheet(q=q, a=a, t=t)
            
        embed = discord.Embed(
            title = f'Added!',
            description = f"{interaction.user.mention} Thank You! This set has been added to the sheet!",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)


    async def on_error(self, interaction:discord.Interaction, error:Exception, /) -> None:
        print(error)
        
        embed = discord.Embed(
            title="Error", 
            description=f'{error}',
            color=discord.Color.red()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def on_timeout(self) -> None: ...

class Add(commands.Cog):
    """Cog for /add command on FaqAiBot
    """
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        print("Add Loaded\n")



    @discord.app_commands.command(name="add",description="Add a question, answer, tag set to the database!")
    async def add(self, interaction:discord.Interaction) -> None:
        try:
            #check for perms
            if interaction.permissions.administrator:
                await interaction.response.send_modal(AddModal())
            else: 
                raise commands.errors.MissingPermissions(missing_permissions= ['administrator'])
            
        #incorrect perms
        except commands.errors.MissingPermissions:

            embed = discord.Embed(
                title = "You do not have permission to do that!",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)



    @add.error
    async def __add_error(self, ctx:commands.Context, error:Exception) -> None:
        logging.log(error)
        
        embed = discord.Embed(
            title = '',
            description=f"Sorry {ctx.author.mention},something went wrong! Please try again...",
            color=discord.Color.red()
        )
        
        await ctx.reply(embed=embed, ephemeral=True)



def add_to_spreadsheet(q:str,a:str,t:str='default_tag') -> None:
    """
    Add the question, answer and tag to the google sheet. (probably prudent to move to mySql server moving forward)

    Args:
    -----------
        q (str): question - will be added to the 'patterns' column.
        a (str): answer - will be added to the 'responses' column.
        t (str, optional): tag - will be added to the 'tag' column. Defaults to 'default_tag', please update either here or in google sheet
    """

    df = sh.get_as_df()

    new_data = pd.DataFrame({
        'patterns' : [q],
        'responses': [a],
        'tag' : [t]
    })

    df = df.append(new_data, ignore_index = True)

    sh.set_dataframe(df, start = 'A1')



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Add(bot))