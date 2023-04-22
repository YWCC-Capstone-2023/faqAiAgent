import os, json, pandas as pd
import discord
from discord.ext import commands

SPREADSHEET = "https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"

def __get_spreadsheet_as_df() -> pd.DataFrame:
    df = pd.read_csv(SPREADSHEET)
    return df


class UpdateModal(discord.ui.Modal, title = "Update a Question and Answer"):
    question = discord.ui.TextInput(
        label = 'Question', 
        required=True, 
        placeholder="Input Question Here",
        style=discord.TextStyle.paragraph
    )

    async def on_submit(self, interaction: discord.Interaction, /) -> None:
        q = self.question
        df = __get_spreadsheet_as_df()

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

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Update(bot))