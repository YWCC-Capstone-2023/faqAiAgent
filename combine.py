import json, os, pandas as pd
import pygsheets
import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
from thefuzz import process, fuzz
from difflib import SequenceMatcher

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scope)

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new")

gc = pygsheets.authorize(service_file='service_account_credentials.json')

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
bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive = True)



def addMe(q,a):
    sh = gc.open('Question and Answers_new')
    print(f"Opened sheet {sh}")
    worksheet1 = sh[0]
    worksheet1.append_table([q,a], start='A104') #list should be question and answer

def trim_all_columns(df:pd.Series):
    trim_strings = lambda s: s.split(';')[0] if ';' in s and isinstance (s,str) else s
    return df.apply(trim_strings)


def measure_accuracy(fuzz_ratio:int, seq_match:float) -> bool:
    seq_match *= 100 
    distance_thresh = 15
    acc_thresh = 70

    distance = abs(fuzz_ratio - round(seq_match))
    # print(f"Distance: {distance}")
    if fuzz_ratio < acc_thresh or seq_match < acc_thresh / 100:
        return False

    if distance > distance_thresh:
        return False

    return True

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def list(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send(df.iloc[3][0]) #iloc[row][col]

@bot.command()
async def ask(ctx, *, content:str):
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new")
    questions = df["Questions"]
    questions = trim_all_columns(questions)

    if ctx.author == bot.user:
        return
    
    message = content

    # print(message)
    '''get the answer for the question that it most closley resembles'''
    ans = process.extractOne(message, questions ,scorer=fuzz.token_set_ratio) 
    # print(f"{ans}\n")

    response = df.iloc[ans[2]][1]

    print(f"Question: {ans[0]}\n")

    print(f"Sequence Match: {SequenceMatcher(None, message, ans[0]).ratio()}")
    print(f"Fuzz accuracy: {ans[1]}")

    # print(f"Response: {response}\n")
    fuzz_ratio = ans[1]
    seq_match = SequenceMatcher(None, message, ans[0]).ratio()

    if measure_accuracy(fuzz_ratio, seq_match):
        await ctx.reply(f'Hi {ctx.message.author.mention}! {response}')
    else:
        await ctx.reply(f'Hi {ctx.message.author.mention}! We could not find this question in our Database. Please @ the professor.')

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

# # 03/24/23
# #ask the group about how to deal with questions not in the database? 
# # 1. create bot command to enter question into the database? 
# #      - implement slash permissions for add_to_db command
# #decide on comparison method to go with for midterm showcase
