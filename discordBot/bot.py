import json, os
import pygsheets
import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

from trainAgent import agent

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'faqAiAgent\credentials\service_account_credentials.json', scope)

gc = pygsheets.authorize(service_file='faqAiAgent\credentials\service_account_credentials.json')

if os.path.exists(os.getcwd() + "\\faqAiAgent\credentials\config.json"):
    with open("faqAiAgent\credentials\config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "\\faqAiAgent\credentials\config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]

 
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive = True)



def addMe(q,a,t='default_tag'):
    sh = gc.open('Question and Answers_new')
    print(f"Opened sheet {sh}")
    worksheet1 = sh[0]
    worksheet1.append_table([q,a,t], start='A104') #list should be question and answer

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ask(ctx, *, content:str):
    if ctx.author == bot.user:
        return
    
    message = content

    author = ctx.message.author.mention

    await ctx.reply(f' Hi {author}! {agent.request(message)}')

@bot.command()
async def add(ctx, *, content:str):
    if ctx.author == bot.user:
        return
    
    '''Cleaning the message to input into DB'''
    a = content.find("?")
    user_question = content[:a+1]
    user_answer = content[a+1:].strip()
    
    print(f"Question: {user_question}\n")
    print(f"Answer: {user_answer}\n")
    addMe(user_question,user_answer)

    await ctx.reply(f'Hi {ctx.message.author.mention}! We have added this question and answer in our Database.')

bot.run(token)