from neuralintents import GenericAssistant
import os, sys

from functions import get_intents

SPREADSHEET = "https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"

if os.path.exists(os.getcwd() + "/intents.json"):
    intents_path = os.getcwd() + "/intents.json"
else:
    #create intents file
    get_intents(SPREADSHEET)

