import logging
import os, json, pandas as pd
from platform import system
from discord.ext import commands
import discord
from neuralintents import GenericAssistant

PATH_TO_INTENTS = os.getcwd() + "\\intents\\" if system() == 'Windows' else os.getcwd() + "/intents/"
PATH_TO_MODEL = os.getcwd() + "\\trained_model\\" if system() == 'Windows' else os.getcwd() + "/trained_model/"


def train_agent() -> GenericAssistant:
    """
    Train AI agent
    """
    
    agent = GenericAssistant(os.path.join(os.getcwd(), PATH_TO_INTENTS, 'intents.json'), model_name='faqAiAgent')

    #check if there already exists some presaved model, speed up the bot login
    #implement method to check for last modified date here
    if os.path.exists(os.path.join(PATH_TO_MODEL, f'{agent.model_name}.h5')):
        agent.load_model(model_name=os.path.join(PATH_TO_MODEL, f'{agent.model_name}'))

    else:
        agent.train_model()
        agent.save_model(model_name= os.path.join(PATH_TO_MODEL, f'{agent.model_name}'))
    
    return agent

class DemoSelect(discord.ui.Select):
    def __init__(self, bot:commands.Bot):
        qList = ['Where is the Kahoot Quiz?','When is the open house?',  'What do I need to bring to the Open House?',                                     'When is the showcase?', 'What is the difference between the brochure and electronic poster board?']

        super().__init__(
            placeholder="Choose a question",
            options=[
                discord.SelectOption(
                    label = question
                )for question in qList
                ]
        )
        self.bot = bot

    async def callback(self, interaction: discord.Interaction) -> None:
        q = self.values[0]

        agent = train_agent()

        response = agent.request(q)

        embed = discord.Embed(
            title = f'{q}',
            description=f'{response}'
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
        
class Demo(commands.Cog):
    """Cog for /Demo command on FaqAiBot
    """
    PATH_TO_INTENTS = ''
    PATH_TO_MODEL = ''
    def __init__(self, bot) -> None:
        self.bot = bot
        print("Demo Loaded\n")
        


    @discord.app_commands.command(name='demo', description="Ask the bot a question!")
    async def demo(self, interaction: discord.Interaction) -> None:
        """ Ask the Bot a question
        """
        
        embed = discord.Embed(
            title = "Demo Ask",
            description="Select Which Question to Ask"
        )
        
        view = discord.ui.View().add_item(DemoSelect(self.bot))

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @demo.error
    async def __demo_error(self, interaction:discord.Interaction, error:Exception) -> None:
        print(error)
        embed = discord.Embed(
            title = "",
            description=f"Sorry {interaction.user.mention},I do not understand! Please ping the Professor!"
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
    



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Demo(bot))