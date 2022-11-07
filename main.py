import requests
import telegram 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import colorama
import json
import re
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')  
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
chat_id = '-1001896645285'
bot = telegram.Bot(token)


options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

nav = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
pegaporcentagem = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')
pegaporcentagem.get('https://tipminer.com/blaze/double')

foradogiro = 1
semutilidade = 0


print(Fore.GREEN + 'BOT INICIADO!')
print(Style.RESET_ALL)
val = []
while True:
    print('No while')
    try:
        try:
            resulROOL = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text

                #Aqui a gente pega a porcentagem de pretos e vermelhos para utlizar no bot.
            porcentagemdepreto = pegaporcentagem.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div/div[2]/div[2]/h5').text
            porcentagemdevermelho = pegaporcentagem.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div/div[2]/div[1]/h5').text

            pegaPretosSeguido = pegaporcentagem.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[6]/div/div[2]/div[2]/h5').text
        except NameError as erro:
           semutilidade = 1
        except Exception as erro:
           semutilidade = 0
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

        pegaPretosSeguidoDividido = "".join(re.findall("\d+", pegaPretosSeguido))
        pegaPretosSeguidoDivididoEmFloat = float(pegaPretosSeguidoDividido)


        porcentagemdepretoDividido = "".join(re.findall("\d+", porcentagemdepreto[3:10]))
        porcentagemdepretoDivididoEmFloat = float(porcentagemdepretoDividido) #Aqui convertemos o numero que pegamos em float

        porcentagemdevermlehoDividido = "".join(re.findall("\d+", porcentagemdevermelho[3:10]))
        porcentagemdevermelhoDivididoEmFloat = float(porcentagemdevermlehoDividido) #Aqui convertemos o numero que pegamos em float
        gale1 = 0
        msg = '''Chegou até aqui!'''
        mensagem = bot.send_message(chat_id=chat_id, text=msg)

        if foradogiro == 1:

            def resultado(num):

                if porcentagemdevermelhoDivididoEmFloat > 4200.0 and porcentagemdepretoDivididoEmFloat < 4500.0 and porcentagemdevermelhoDivididoEmFloat > porcentagemdepretoDivididoEmFloat:
    #==========================================Estrategia Sequencia============================#


                    if num[0:4] == ['P', 'P', 'P', 'P']:
                        if gale1 == 1 and num[0:5] == ['P', 'P', 'P', 'P', 'P']:
                            gale1 = 0
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.RED + '==LOSS==')
                            print(Style.RESET_ALL)
                            return

                        elif gale == 1 and num[0:5] == ['V', 'P', 'P', 'P', 'P']:
                            msg = '''✅GALE 1 GREEN no 🔴🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.RED + '==GALE 1 WIN==')
                            print(Style.RESET_ALL)
                            gale1 = 0
                            return
                        elif gale1 == 1 and num[0:5] == ['B', 'P', 'P', 'P', 'P']:
                            gale1 = 0
                            msg = '''✅GALE 1 GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.RED + '==LOSS==')
                            print(Style.RESET_ALL)
                            return

                        elif num[0:5] == ['P', 'P', 'P', 'P', 'P']:
                            return

                        elif num[0:4] == ['P', 'P', 'P', 'P']:
                            gale1 = 1
                            msg = '''GALE 1'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.YELLOW + '==GALE 1==')
                            print(Style.RESET_ALL)
                            return



                    elif num[0:4] == ['V', 'P', 'P', 'P']:

                        if num[0:5] == ['V', 'P', 'P', 'P', 'P']:
                            return

                        elif num[0:4] == ['V', 'P', 'P', 'P']:
                            msg = '''✅ GREEN no 🔴🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return
                        elif num[0:4] == ['B', 'P', 'P', 'P']:
                            msg = '''✅ GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return


                    elif num[0:3] == ['P', 'P', 'P']:

                        if num[0:4] == ['P', 'P', 'P', 'P']:
                            return

                        elif num[0:3] == ['P', 'P', 'P']:
                            msg = '''🚨Entrada confirmada🚨
📌Entrar no 🔴 
🛡️Proteger o ⚪'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return


                    elif num[0:2] == ['P', 'P']:
 
                       if num[0:3] == ['P', 'P', 'P']:
                            return

                       elif num[0:2] == ['P', 'P']:
                            msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no 🔴 
⏰Aguarde o sinal...'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            time.sleep(15)
                            mensagem.delete()
                            if resulROOL == 'Girando...':
                               return
                            return





                elif porcentagemdepretoDivididoEmFloat > 4700.0 and porcentagemdevermelhoDivididoEmFloat < 4400.0 and porcentagemdepretoDivididoEmFloat > porcentagemdevermelhoDivididoEmFloat:
    #==========================================Estrategia Sequencia============================#
                    if num[0:4] == ['V', 'V', 'V', 'V']:
                        if num[0:5] == ['V', 'V', 'V', 'V', 'V']:
                            return

                        elif num[0:4] == ['V', 'V', 'V', 'V']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.RED + '==LOSS==')
                            print(Style.RESET_ALL)
                            return


                    elif num[0:4] == ['P', 'V', 'V', 'V']:

                        if num[0:5] == ['P', 'V', 'V', 'V', 'V']:
                            return

                        elif num[0:4] == ['P', 'V', 'V', 'V']:
                            msg = '''✅ GREEN no ⚫🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return
                        elif num[0:4] == ['B', 'V', 'V', 'V']:
                            msg = '''✅ GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return


                    elif num[0:3] == ['V', 'V', 'V']:

                        if num[0:4] == ['V', 'V', 'V', 'V']:
                            return

                        elif num[0:3] == ['V', 'V', 'V']:
                            msg = '''🚨Entrada confirmada🚨
📌Entrar no ⚫ 
🛡️Proteger o ⚪'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return


                    elif num[0:2] == ['V', 'V']:
 
                       if num[0:3] == ['V', 'V', 'V']:
                            return

                       elif num[0:2] == ['P', 'P']:
                            msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no ⚫ 
⏰Aguarde o sinal...'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            time.sleep(15)
                            mensagem.delete()
                            if resulROOL == 'Girando...':
                               return
                            return


        #==========================================FIM========================================#

    #==========================================ESTRATEGIA MATADORA========================================#
                elif porcentagemdevermelhoDivididoEmFloat > 4700.0 and porcentagemdepretoDivididoEmFloat < 4400.0 and porcentagemdevermelhoDivididoEmFloat > porcentagemdepretoDivididoEmFloat:


                    if num[0:4] == ['V', 'B', 'V', 'V']:
                        if num[0:5] == ['V', 'B', 'V', 'V', 'V']:
                            return

                        elif  num[0:4] == ['V', 'B', 'V', 'V']:
                            msg = '''✅ GREEN no 🔴🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return
                        elif  num[0:4] == ['B', 'B', 'V', 'V']:
                            msg = '''✅ GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return


                    elif num[0:4] == ['P', 'B', 'V', 'V']:

                        if num[0:5] == ['P', 'B', 'V', 'V', 'V']:
                            return

                        elif  num[0:4] == ['P', 'B', 'V', 'V']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.RED + '==LOSS==')
                            print(Style.RESET_ALL)
                            return


                    elif num[0:3] == ['B', 'V', 'V']:

                        if num[0:4] == ['B', 'V', 'V', 'V']:
                            return

                        elif num[0:3] == ['B', 'V', 'V']:
                            msg = '''🚨Entrada confirmada!! Este é o metodo de porcentagem!!!!🚨
📌Entrar no 🔴 
🛡️Proteger o ⚪'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return

                        elif num[0:2] == ['V', 'V']:
                            msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no 🔴 
⏰Aguarde o sinal...'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            time.sleep(15)
                            mensagem.delete()
                            if resulROOL == 'Girando...':
                               return
                            return
 





                elif porcentagemdepretoDivididoEmFloat > 4700.0 and porcentagemdevermelhoDivididoEmFloat < 4400.0 and porcentagemdepretoDivididoEmFloat > porcentagemdevermelhoDivididoEmFloat:

                        if  num[0:4] == ['P', 'B', 'P', 'P']:
                            msg = '''✅ GREEN no ⚫🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return
                        elif  num[0:4] == ['B', 'B', 'P', 'P']:
                            msg = '''✅ GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            print(Fore.GREEN + '==WIN!!!==')
                            print(Style.RESET_ALL)
                            return

                        elif num[0:4] == ['V', 'B', 'P', 'P']:
                            if num[0:5] == ['V', 'B', 'P', 'P', 'P']:
                                return

                            elif  num[0:4] == ['V', 'B', 'P', 'P']:
                                msg = '''❌LOSS'''
                                mensagem = bot.send_message(chat_id=chat_id, text=msg)
                                print(Fore.RED + '==LOSS==')
                                print(Style.RESET_ALL)
                                return

                        elif num[0:3] == ['B', 'P', 'P']:

                            if num[0:4] == ['B', 'P', 'P', 'P']:
                                return

                            elif num[0:3] == ['B', 'P', 'P']:
                                msg = '''🚨Entrada confirmada!! Este é o metodo de porcentagem!!!!🚨
📌Entrar no ⚫ 
🛡️Proteger o ⚪'''
                                mensagem = bot.send_message(chat_id=chat_id, text=msg)
                                return

                            elif num[0:2] == ['P', 'P']:
                                msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no ⚫ 
⏰Aguarde o sinal...'''
                                mensagem = bot.send_message(chat_id=chat_id, text=msg)
                                time.sleep(15)
                                mensagem.delete()
                                if resulROOL == 'Girando...':
                                   return
                                return
    #==========================================FIM========================================#
            foradogiro = 0
            resultado(ray)
            print(Fore.BLUE)
            print('Porcentagem preto:', porcentagemdepretoDivididoEmFloat)
            print('Porcentagem vermelho:', porcentagemdevermelhoDivididoEmFloat)
            print(Style.RESET_ALL)
            print('Cores da rodada:',ray)
            print(Fore.YELLOW + 'FIM DA RODADA!')
            print(Style.RESET_ALL)


    #except NameError as erro:
        #semutilidade = 1
    #except Exception as erro:
        #semutilidade = 0
    finally:
        print('FIM.')


nav.quit()
pegaporcentagem.quit()
