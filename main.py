import requests
import telegram 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import colorama
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
chat_id = '-1001896645285'
bot = telegram.Bot(token)


nav = webdriver.Chrome(options = chrome_options)
nav.get('https://blaze.com/pt/games/double')

foradogiro = 0
semutilidade = 0
gale = 0
teste = 0


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

    except NameError as erro:
        semutilidade = 0
    except Exception as erro:
        semutilidade = 0
    #finally:
        #print('FIM.')
        
        if resulROOL == 'Girando...':
            foradogiro = 1
        if foradogiro == 1 and resulROOL != 'Girando...':

            def resultado(num):
                global gale #Pra não bugar a variavel "gale"
                
                #if porcentagemdevermelhoDivididoEmFloat > 4200.0 and porcentagemdepretoDivididoEmFloat < 4500.0 and porcentagemdevermelhoDivididoEmFloat > porcentagemdepretoDivididoEmFloat:
                if teste == 0:
    #==========================================Estrategia Sequencia============================#
                #================================GALE 1===============================#

                    if gale == 1:
                        if num[0:5] == ['P', 'P', 'P', 'P', 'P']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['V', 'P', 'P', 'P', 'P']:
                            msg = '''✅G1 GREEN no 🔴🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['B', 'P', 'P', 'P', 'P']:
                            msg = '''✅G1 GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                #===============================================================#

                    elif num[0:4] == ['P', 'P', 'P', 'P']:
                        if num[0:5] == ['P', 'P', 'P', 'P', 'P']:
                            return

                        elif num[0:4] == ['P', 'P', 'P', 'P']:
                            msg = '''GALE 1'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 1
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



                #elif porcentagemdepretoDivididoEmFloat > 4700.0 and porcentagemdevermelhoDivididoEmFloat < 4400.0 and porcentagemdepretoDivididoEmFloat > porcentagemdevermelhoDivididoEmFloat:
                if teste == 0:
    #==========================================Estrategia Sequencia============================#

                #================================GALE 1===============================#
                    if gale == 1:
                        if num[0:5] == ['V', 'V', 'V', 'V', 'V']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['P', 'V', 'V', 'V', 'V']:
                            msg = '''✅G1 GREEN no ⚫🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['B', 'V', 'V', 'V', 'V']:
                            msg = '''✅G1 GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                #===============================================================#


                    elif num[0:4] == ['V', 'V', 'V', 'V']:
                        if num[0:5] == ['V', 'V', 'V', 'V', 'V']:
                            return

                        elif num[0:4] == ['V', 'V', 'V', 'V']:
                            msg = '''GALE 1'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 1
                            return


                    elif num[0:4] == ['P', 'V', 'V', 'V']:

                        if num[0:5] == ['P', 'V', 'V', 'V', 'V']:
                            return

                        elif num[0:4] == ['P', 'V', 'V', 'V']:
                            msg = '''✅ GREEN no ⚫🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return

                        elif num[0:4] == ['B', 'V', 'V', 'V']:
                            msg = '''✅ GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
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

                        elif num[0:2] == ['V', 'V']:
                            msg = '''⚠️ATENÇÃO⚠️
Possivel entrada no ⚫ 
⏰Aguarde o sinal...'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            time.sleep(15)
                            mensagem.delete()
                            if resulROOL == 'Girando...':
                               return
                            return

#===================================================FIM==================================================#



                if teste == 0:
    #==========================================Estrategia MATADORA NO VERMELHO============================#

                #================================GALE 1===============================#
                    if gale == 1:
                        if num[0:5] == ['P', 'P', 'B', 'V', 'V']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['V', 'P', 'B', 'V', 'V']:
                            msg = '''✅G1 GREEN no 🔴🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['B', 'P', 'B', 'V', 'V']:
                            msg = '''✅G1 GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                #===============================================================#


                    elif num[0:4] == ['P', 'B', 'V', 'V']:
                        if num[0:5] == ['P', 'B', 'V', 'V', 'V']:
                            return

                        elif num[0:4] == ['P', 'B', 'V', 'V']:
                            msg = '''GALE 1'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 1
                            return



                    elif num[0:4] == ['B', 'V', 'V', 'V']:
                        return

                    elif num[0:4] == ['V', 'B', 'V', 'V']:
                        msg = '''✅ GREEN no 🔴🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return
                    elif num[0:4] == ['B', 'B', 'V', 'V']:
                        msg = '''✅ GREEN no ⚪🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return

                    elif num[0:3] == ['B', 'V', 'V']:

                        if num[0:4] == ['B', 'V', 'V', 'V']:
                            return

                        elif num[0:3] == ['B', 'V', 'V']:
                            msg = '''🚨Entrada confirmada🚨
📌Entrar no 🔴 
🛡️Proteger o ⚪'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return
#===================================================FIM==================================================#

                if teste == 0:
    #==========================================Estrategia MATADORA NO PRETO============================#

                #================================GALE 1===============================#
                    if gale == 1:
                        if num[0:5] == ['V', 'V', 'B', 'P', 'P']:
                            msg = '''❌LOSS'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['P', 'V', 'B', 'P', 'P']:
                            msg = '''✅G1 GREEN no ⚫🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                        elif num[0:5] == ['B', 'P', 'B', 'P', 'P']:
                            msg = '''✅G1 GREEN no ⚪🍷🗿'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 0
                            return

                #===============================================================#


                    elif num[0:4] == ['V', 'B', 'P', 'P']:
                        if num[0:5] == ['V', 'B', 'P', 'P', 'P']:
                            return

                        elif num[0:4] == ['V', 'B', 'P', 'P']:
                            msg = '''GALE 1'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            gale = 1
                            return



                    elif num[0:4] == ['B', 'P', 'P', 'P']:
                        return

                    elif num[0:4] == ['P', 'B', 'P', 'P']:
                        msg = '''✅ GREEN no ⚫🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return
                    elif num[0:4] == ['B', 'B', 'P', 'P']:
                        msg = '''✅ GREEN no ⚪🍷🗿'''
                        mensagem = bot.send_message(chat_id=chat_id, text=msg)
                        return

                    elif num[0:3] == ['B', 'P', 'P']:

                        if num[0:4] == ['B', 'P', 'P', 'P']:
                            return

                        elif num[0:3] == ['B', 'P', 'P']:
                            msg = '''🚨Entrada confirmada🚨
📌Entrar no ⚫ 
🛡️Proteger o ⚪'''
                            mensagem = bot.send_message(chat_id=chat_id, text=msg)
                            return
#===================================================FIM==================================================#

            foradogiro = 0
            resultado(ray)

nav.quit()
#pegaporcentagem.quit()
