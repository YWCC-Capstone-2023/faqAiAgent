import json, os, logging

import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

HANDLER = logging.FileHandler(
    filename='docs/discord.log', 
    encoding='utf-8', 
    mode='w'
)

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

if os.path.exists("credentials/service_account_credentials.json"):
    CREDS = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials/service_account_credentials.json', SCOPE)
else:
    print('service_account_credentials.json missing...aborting...')
    exit(1)

if os.path.exists("credentials/config.json"):
    with open("credentials/config.json") as f:
        configData = json.load(f)
else:
    print("config.json missing...aboring...")
    exit(1)
    
TOKEN = configData["Token"]
PREFIX = configData["Prefix"]


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

    #load all commands present in /cogs/
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename not in ['update.py']: #update still in dev, do not load
            await bot.load_extension(f'cogs.{filename[:-3]}')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")

    except Exception as e:
        print(e)

    print('We have logged in as {0.user}'.format(bot))

bot.run(TOKEN, log_handler=HANDLER, log_level=logging.WARNING)