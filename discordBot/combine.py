import json, os
import pygsheets
import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

from trainBot import agent

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    '/credentials/service_account_credentials.json', scope)

gc = pygsheets.authorize(service_file='/credentials/service_account_credentials.json')

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./credentials/config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/credentials/config.json", "w+") as f:
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

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ask(ctx, *, content:str):
    # df = pd.read_csv("https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new")
    # questions = df["Questions"]
    # questions = trim_all_columns(questions)

    # if ctx.author == bot.user:
    #     return
    
    # message = content

    # # print(message)
    # '''get the answer for the question that it most closley resembles'''
    # ans = process.extractOne(message, questions ,scorer=fuzz.token_set_ratio) 
    # # print(f"{ans}\n")

    # response = df.iloc[ans[2]][1]

    # print(f"Question: {ans[0]}\n")

    # print(f"Sequence Match: {SequenceMatcher(None, message, ans[0]).ratio()}")
    # print(f"Fuzz accuracy: {ans[1]}")

    # # print(f"Response: {response}\n")
    # fuzz_ratio = ans[1]
    # seq_match = SequenceMatcher(None, message, ans[0]).ratio()

    # if measure_accuracy(fuzz_ratio, seq_match):
    #     await ctx.reply(f'Hi {ctx.message.author.mention}! {response}')
    # else:
    #     await ctx.reply(f'Hi {ctx.message.author.mention}! We could not find this question in our Database. Please @ the professor.')

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
