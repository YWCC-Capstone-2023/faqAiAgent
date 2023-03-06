import discord
import gspread
import pandas as pd

from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

import json
import os

"""google sheet credential setup"""
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scope)


'''
Link to download CSV of spreadsheet for Pandas Manipulation
https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new
'''
client = gspread.authorize(credentials = creds)
faq_sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/edit#gid=2019565985')
sheet_instance = faq_sheet.get_worksheet(0)

questions = sheet_instance.col_values(1)
answers = sheet_instance.col_values(3)
# print(faq_sheet, "\n")
# print(questions, "\n")
# print(answers, "\n")


url = f"https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"
print(pd.read_csv(url))
print("done")
# if os.path.exists(os.getcwd() + "/config.json"):``
#     with open("./config.json") as f:
#         configData = json.load(f)

# else:
#     configTemplate = {"Token": "", "Prefix": "!"}

#     with open(os.getcwd() + "/config.json", "w+") as f:
#         json.dump(configTemplate, f) 

# token = configData["Token"]
# prefix = configData["Prefix"]

 
# intents = discord.Intents.all()
# client = discord.Client(command_prefix='!', intents=intents)
# print("here")


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
 
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
 
#     if message.content.startswith('!'):
#         await message.channel.send('Message Read!')
 
# client.run(token)
