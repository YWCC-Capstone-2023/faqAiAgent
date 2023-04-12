import os,time

import gspread
from neuralintents import GenericAssistant

from functions import get_intents


SPREADSHEET = "https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"

get_intents(SPREADSHEET)

agent = GenericAssistant('intents.json', model_name='faqAgent')

if os.path.isfile(f'{agent.model_name}.h5'):
    agent.load_model()
else:
    agent.train_model()
    agent.save_model()