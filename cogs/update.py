import os, json, logging, pandas as pd

import discord
from discord.ext import commands

import pygsheets

# setup access to spreadsheet
path_to_creds = os.path.join(os.getcwd(), 'credentials', 'service_account_credentials.json')

if os.path.exists(path_to_creds):
    gc = pygsheets.authorize(service_file=path_to_creds)

else: logging.log(msg='Failed to Load Service Account Credentials for spreasheet')

sh = gc.open('Question and Answers_new').sheet1

class UpdateModal(discord.ui.Modal, title = "Update a Question and Answer"):
    """currently in development"""
    question = discord.ui.TextInput(
        label = 'Question', 
        required=True, 
        placeholder="Input Question Here",
        style=discord.TextStyle.paragraph
    )

    async def on_submit(self, interaction: discord.Interaction, /) -> None:
        q = self.question

        df = sh.get_as_df()

        target = df[df['patterns'].str.contains(q).index]

        mask = df['patterns'].str.contains(q)

        if mask.any():
            first_index = mask.idxmax()
        else:
            # throw an embed
            print("Question not found in database!")


        row = df.iloc[first_index]
        question = row['patterns']
        answer = row['responses']
        tag = row['tag']

        print(f"Grabbed: {question}, {answer}, {tag}")

        print(f'Target Row {target}')


class Update(commands.Cog):
     
    def __init__(self, bot) -> None:
            self.bot = bot
            print("Update Loaded\n")

    
    @discord.app_commands.command(name='update', description="Update a question/answer/tag in the database!")
    async def update(self, interaction: discord.Interaction) -> None:
        

        await interaction.response.send_modal(UpdateModal())


        #slash update with q/a/tag
        #modal pop up
            #in the modal, ask question to update and depending tag, what you wanna update
            #the tag to 
    
    @update.error
    async def __update_error(self, interaction:discord.Interaction, error) -> None:
        print(error)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Update(bot))