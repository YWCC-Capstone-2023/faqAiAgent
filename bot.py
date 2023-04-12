import json, os
import pygsheets
import discord
from discord.ext import commands
from discord import app_commands
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
bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive = True, help_command=None)


def is_owner() -> bool:
    def predicate(interaction: discord.Interaction):
        return interaction.user.id == interaction.guild.owner_id
    return app_commands.check(predicate=predicate)

def addMe(q,a,t='default_tag'):
    sh = gc.open('Question and Answers_new')
    print(f"Opened sheet {sh}")
    worksheet1 = sh[0]
    worksheet1.append_table([q,a,t], start='A104') #list should be question and answer

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    try:
        synced = await bot.tree.sync
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="ask")
@app_commands.describe(question = "What is your question?")
async def ask(interaction: discord.Interaction, question:str):
    response = agent.request(question)
    await interaction.response.send_message(f"Hi {interaction.user.mention}! {response}", ephermal = True)

@bot.tree.command(name="add")
@app_commands.describe(question = "What is your question?", answer = "What is the answer?")
@is_owner()
async def add(interaction: discord.Interaction, question:str, answer:str):
    # a = content.find("?")
    # user_question = content[:a+1]
    # user_answer = content[a+1:].strip()
    
    print(f"Question: {question}\n")
    print(f"Answer: {answer}\n")
    addMe(question,answer)

    await interaction.response.send_message(f"{interaction.user.mention} We have added this question and answer in our Database.", ephermal = True)

@add.error
async def add_error(interaction: discord.Interaction, error):
    await interaction.response.send_message("Sorry! You do not have permission to execute this command!", ephemeral=True)

bot.run(token)