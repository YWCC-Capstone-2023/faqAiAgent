from discord.ext import commands
import discord
import pygsheets
import os

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        if os.path.exists('credentials/service_account_credentials.json'):
            self.gc = pygsheets.authorize(service_file='credentials/service_account_credentials.json')
        else:
            pass

        print("Add Loaded\n")

    @commands.hybrid_command(name="add", description= "Add a question, answer, topic set to the database!",guild_ids=[1072948383955816459])
    @commands.has_any_role(["Professor", "Operations", "Team Member", "Server Admin"])
    async def add(self,ctx: discord.Interaction, question:str, answer:str, topic:str = "default_tag"):
        print(f"Question: {question}\n")
        print(f"Answer: {answer}\n")
        print(f'Topic: {topic}')

        self.addMe(question,answer,topic)
        await ctx.reply(f"{ctx.author.mention} We have added this question and answer in our Database.", ephermal = True)

    @add.error
    async def __add_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.reply(f"You do not have permission to do that!", ephemeral=True)
        else:
            await ctx.reply(f"Sorry {ctx.author.mention},I do not understand! Please ping the Professor!", ephemeral=True)

    def __addMe(self,q,a,t='default_tag'):
        sh = self.gc.open('Question and Answers_new')
        worksheet1 = sh[0]
        worksheet1.append_table([q,a,t], start='A104') #list should be question and answer


    
async def setup(bot):
    await bot.add_cog(Add(bot))