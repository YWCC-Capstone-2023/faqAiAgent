from discord.ext import commands
import discord
import pygsheets

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gc = pygsheets.authorize(service_file='service_account_credentials.json')
        print("Add Loaded\n")

    @commands.hybrid_command(name="add")
    async def add(self, ):
        pass

    async def add(self,interaction: discord.Interaction, question:str, answer:str):
        # a = content.find("?")
        # user_question = content[:a+1]
        # user_answer = content[a+1:].strip()
        
        print(f"Question: {question}\n")
        print(f"Answer: {answer}\n")
        self.addMe(question,answer)

        await interaction.response.send_message(f"{interaction.user.mention} We have added this question and answer in our Database.", ephermal = True)

    @add.error
    async def __add_error(self,interaction: discord.Interaction, error):
        await interaction.response.send_message("Sorry! You do not have permission to execute this command!", ephemeral=True)

    def __is_owner(self) -> bool:
        def predicate(interaction: discord.Interaction):
            return interaction.user.id == interaction.guild.owner_id
        return discord.app_commands.check(predicate=predicate)

    def __addMe(self,q,a,t='default_tag'):
        sh = self.gc.open('Question and Answers_new')

        worksheet1 = sh[0]
        worksheet1.append_table([q,a,t], start='A104') #list should be question and answer


    
async def setup(bot):
    await bot.add_cog(Add(bot))