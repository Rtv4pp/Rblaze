import requests
import telegram 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import telegram
import os
import colorama
import json
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')    

token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
chat_id = '-1001896645285'
bot = telegram.Bot(token)

nav.get('https://blaze.com/pt/games/double')

foradogiro = 0
semutilidade = 0


os.system('cls') or None
print(Fore.GREEN + 'BOT INICIADO!')
print(Style.RESET_ALL)

while True:

    try:

        resulROOL = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text

        url = 'https://blaze.com/api/roulette_games/recent'

        response = requests.get(url)

        r = response.json()

        ray = []

        for x in range(len(r)):
            val = r[x]['color']
            if val == 1:
                val = 'V'

            if val == 2:
                val = 'P'

            if val == 0:
                val = 'B'

            ray.append(val)





        if resulROOL == 'Girando...':
            foradogiro = 1

        if foradogiro == 1 and resulROOL != 'Girando...':

            def resultado(num):

    #==========================================Estrategia Sequencia============================#

                if num[0:3] == ['V', 'P', 'P']:

                    if num[0:4] == ['V', 'P', 'P', 'P']:
                        return

                    elif num[0:3] == ['V', 'P', 'P']:
                        msg = '''❌LOSS'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return


                elif num[0:3] == ['P', 'P', 'P']:

                    if num[0:4] == ['P', 'P', 'P', 'P']:
                        return

                    elif num[0:3] == ['P', 'P', 'P']:
                        msg = '''✅ GREEN no ⚫🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return
                    elif num[0:3] == ['B', 'P', 'P']:
                        msg = '''✅ GREEN no ⚪🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return

                elif num[0:2] == ['P', 'P']:

                    if num[0:3] == ['P', 'P', 'P']:
                        return

                    elif num[0:2] == ['P', 'P']:
                        msg = '''🚨Entrada confirmada🚨
📌Entrar no ⚫ 
🛡️Proteger o ⚪'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return


                elif num[0:1] == ['P']:

                    if num[0:2] == ['P', 'P']:
                        return

                    elif num[0:1] == ['P']:
                        msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no ⚫ 
⏰Aguarde o sinal...'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return

    #==========================================FIM========================================#

            foradogiro = 0
            resultado(ray)
            print(ray)
            print(Fore.YELLOW + 'FIM DA RODADA!')
            print(Style.RESET_ALL)








    except NameError as erro:
        semutilidade = 1
    except Exception as erro:
        semutilidade = 0
