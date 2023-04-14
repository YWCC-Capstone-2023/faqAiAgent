import os

from discord.ext import commands
import discord

import pygsheets

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
    


    async def on_submit(self, interaction: discord.Interaction, /) -> None:
        q = self.question
        a = self.answer
        t = self.tag

        addMe(q=q, a=a, t=t)
        await interaction.response.send_message(f"{interaction.user.mention} Thank You! This set has been added to the sheet!")
    


    async def on_error(self, interaction: discord.Interaction, error: Exception, /) -> None:
        return await super().on_error(interaction, error)


class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Add Loaded\n")



    @commands.hybrid_command(name="add", description= "Add a question, answer, topic set to the database!",guild_ids=[1072948383955816459])
    @commands.has_any_role(["Professor", "Operations", "Team Member", "Server Admin"])
    async def add(self,ctx: discord.Interaction):
        await ctx.response.send_modal(AddModal())


    @add.error
    async def __add_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.reply(f"You do not have permission to do that!", ephemeral=True)
        else:
            await ctx.reply(f"Sorry {ctx.author.mention},I do not understand! Please ping the Professor!", ephemeral=True)



def addMe(self,q,a,t='default_tag'):
    if os.path.exists('../credentials/service_account_credentials.json'):
        self.gc = pygsheets.authorize(service_file='../credentials/service_account_credentials.json')
    else: pass

    sh = self.gc.open('Question and Answers_new')
    worksheet1 = sh[0]
    worksheet1.append_table([q,a,t], start='A104')



async def setup(bot):
    await bot.add_cog(Add(bot))