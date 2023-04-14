import json, os

import pygsheets
import discord
from discord.ext import commands
from discord import app_commands
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials/service_account_credentials.json', scope)


if os.path.exists("credentials/config.json"):
    with open("credentials/config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "credentials/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

 
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive = True, help_command=None)

@bot.command()
async def load(ctx:commands.Context, cog:commands.Cog):
    bot.load_extension(f'cogs.{cog}')

@bot.command()
async def unLoad(ctx:commands.Context, cog:commands.Cog):
    bot.unload_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

bot.run(token)