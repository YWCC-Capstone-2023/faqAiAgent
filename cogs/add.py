import logging
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
    

    """on_submit -> return all of the modal text inputs
    """
    async def on_submit(self, interaction: discord.Interaction, /) -> None:
        q = self.question
        a = self.answer
        t = self.tag

        add_to_spreadsheet(q=q, a=a, t=t)
        
        await interaction.response.send_message(f"{interaction.user.mention} Thank You! This set has been added to the sheet!", ephemeral=True)



    async def on_error(self, interaction:discord.Interaction, error:Exception, /) -> None:
        return await super().on_error(interaction, error)


    async def on_timeout(self) -> None:
        ...

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
                raise commands.errors.MissingPermissions
            
        #incorrect perms
        except commands.errors.MissingPermissions:

            embed = discord.Embed(
                title = "You are missing the correct permission(s) to run this command!",
                description=""
            )
            await interaction.response.send_message(f"You do not have permission to do that!", ephemeral=True)



    @add.error
    async def __add_error(self, ctx:commands.Context, error:Exception) -> None:
        logging.log(error)
        
        embed = discord.Embed(
            title = '',
            description=f"Sorry {ctx.author.mention},something went wrong! Please try again..."
        )
        
        await ctx.reply(embed, ephemeral=True)



def add_to_spreadsheet(self,q:str,a:str,t:str='default_tag') -> None:
    """
    Add the question, answer and tag to the google sheet. (probably prudent to move to mySql server moving forward)

    Args:
    -----------
        q (str): question - will be added to the 'patterns' column.
        a (str): answer - will be added to the 'responses' column.
        t (str, optional): tag - will be added to the 'tag' column. Defaults to 'default_tag', please update either here or in google sheet
    """
    if os.path.exists('/credentials/service_account_credentials.json'):
        self.gc = pygsheets.authorize(service_file='/credentials/service_account_credentials.json')
    else: pass

    sh = self.gc.open('Question and Answers_new')
    worksheet1 = sh[0]

    #change this from 'A104' to whatever the first empty cell is
    worksheet1.append_table([q,a,t], start='A1')



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Add(bot))