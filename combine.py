import discord
import gspread
import pandas as pd
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import json
import os

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scope)

client = gspread.authorize(credentials = creds)
mainSheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/edit#gid=2019565985')

worksheet = mainSheet.worksheet('Questions')
df_read = get_as_dataframe(worksheet, usecols=[0], nrows=10, header=0, skiprows=None)
print(df_read.iloc[0])
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

 
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def list(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send(df_read)
    
   

bot.run(token)