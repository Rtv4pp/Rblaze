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
import re

PROXY = '177.182.135.88:3128'
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'--proxy-server={PROXY}')

try:
  #nav = requests.Session()
  #nav.proxies = {"http": "191.242.187.82:3218"}

  #pegaporcentagem = requests.Session()
  #pegaporcentagem.proxies = {"http": "191.242.187.82:3218"}

  token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
  chat_id = '-1001896645285'
  bot = telegram.Bot(token)

  nav = webdriver.Chrome(options=chrome_options)
  nav.get('https://blaze.com/pt/games/double')

  pegaporcentagem = webdriver.Chrome(options=chrome_options)
  pegaporcentagem.get('https://tipminer.com/blaze/double')

  foradogiro = 0
  semutilidade = 0
  gale = 0
  teste = 0

except NameError as erro:
  semutilidade = 0
  print('VIXI deu o erro 1')
except Exception as erro:
  semutilidade = 0
  print('VIXI deu o erro 2')

os.system('cls') or None
print(Fore.GREEN + 'BOT INICIADO!')
print(Style.RESET_ALL)

while True:

  try:
    resulROOL = nav.find_element(By.XPATH,
                                 '//*[@id="roulette-timer"]/div[1]').text

    porcentagemdepreto = pegaporcentagem.find_element(
      By.XPATH,
      '//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/h5'
    ).text
    porcentagemdevermelho = pegaporcentagem.find_element(
      By.XPATH,
      '//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/h5'
    ).text

    porcentagemdepretoDividido = "".join(
      re.findall("\d+", porcentagemdepreto[3:10]))
    porcentagemdepretoDivididoEmFloat = float(
      porcentagemdepretoDividido
    )  #Aqui convertemos o numero que pegamos em float

    porcentagemdevermlehoDividido = "".join(
      re.findall("\d+", porcentagemdevermelho[3:10]))
    porcentagemdevermelhoDivididoEmFloat = float(
      porcentagemdevermlehoDividido
    )  #Aqui convertemos o numero que pegamos em float

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
        global gale  #Pra não bugar a variavel "gale"

        #if porcentagemdevermelhoDivididoEmFloat > 4200.0 and porcentagemdepretoDivididoEmFloat < 4500.0 and porcentagemdevermelhoDivididoEmFloat > porcentagemdepretoDivididoEmFloat:
        if teste == 0:
          #==========================================Estrategia Sequencia============================#
          #================================GALE 1===============================#

          if gale == 1:
            if num[0:5] == ['P', 'P', 'P', 'P', 'P']:
              msg = '''❌LOSS'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.RED + '==LOSS==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['V', 'P', 'P', 'P', 'P']:
              msg = '''✅G1 GREEN no 🔴🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['B', 'P', 'P', 'P', 'P']:
              msg = '''✅G1 GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

        #===============================================================#

          elif num[0:4] == ['P', 'P', 'P', 'P']:
            if num[0:5] == ['P', 'P', 'P', 'P', 'P']:
              return

            elif num[0:4] == ['P', 'P', 'P', 'P']:
              msg = '''GALE 1'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.YELLOW + 'GALE 1')
              print(Style.RESET_ALL)
              gale = 1
              return

          elif num[0:4] == ['V', 'P', 'P', 'P']:

            if num[0:5] == ['V', 'P', 'P', 'P', 'P']:
              return

            elif num[0:4] == ['V', 'P', 'P', 'P']:
              msg = '''✅ GREEN no 🔴🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              return
            elif num[0:4] == ['B', 'P', 'P', 'P']:
              msg = '''✅ GREEN no ⚪🍷🗿'''
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
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
              print(Fore.RED + '==LOSS==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['P', 'V', 'V', 'V', 'V']:
              msg = '''✅G1 GREEN no ⚫🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['B', 'V', 'V', 'V', 'V']:
              msg = '''✅G1 GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

        #===============================================================#

          elif num[0:4] == ['V', 'V', 'V', 'V']:
            if num[0:5] == ['V', 'V', 'V', 'V', 'V']:
              return

            elif num[0:4] == ['V', 'V', 'V', 'V']:
              msg = '''GALE 1'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.YELLOW + '==GALE 1==')
              print(Style.RESET_ALL)
              gale = 1
              return

          elif num[0:4] == ['P', 'V', 'V', 'V']:

            if num[0:5] == ['P', 'V', 'V', 'V', 'V']:
              return

            elif num[0:4] == ['P', 'V', 'V', 'V']:
              msg = '''✅ GREEN no ⚫🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              return

            elif num[0:4] == ['B', 'V', 'V', 'V']:
              msg = '''✅ GREEN no ⚪🍷🗿'''
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
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

#elif porcentagemdepretoDivididoEmFloat < 4300 and porcentagemdevermelhoDivididoEmFloat > 4500:
        if teste == 0:
          #==========================================Estrategia MATADORA NO VERMELHO============================#

          #================================GALE 1===============================#
          if gale == 1:
            if num[0:5] == ['P', 'P', 'B', 'V', 'V']:
              msg = '''❌LOSS'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.RED + '==LOSS==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['V', 'P', 'B', 'V', 'V']:
              msg = '''✅G1 GREEN no 🔴🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['B', 'P', 'B', 'V', 'V']:
              msg = '''✅G1 GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

        #===============================================================#

          elif num[0:4] == ['P', 'B', 'V', 'V']:
            if num[0:5] == ['P', 'B', 'V', 'V', 'V']:
              return

            elif num[0:4] == ['P', 'B', 'V', 'V']:
              msg = '''GALE 1'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.YELLOW + '==GALE 1==')
              print(Style.RESET_ALL)
              gale = 1
              return

          elif num[0:4] == ['V', 'B', 'V', 'V']:

            if num[0:5] == ['B', 'V', 'V', 'V', 'V']:
              return

            elif num[0:4] == ['V', 'B', 'V', 'V']:
              msg = '''✅ GREEN no 🔴🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              return
            elif num[0:4] == ['B', 'B', 'V', 'V']:
              msg = '''✅ GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
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

#elif porcentagemdepretoDivididoEmFloat > 4500 and porcentagemdevermelhoDivididoEmFloat < 4300:
        if teste == 0:
          #==========================================Estrategia MATADORA NO PRETO============================#

          #================================GALE 1===============================#
          if gale == 1:
            if num[0:5] == ['V', 'V', 'B', 'P', 'P']:
              msg = '''❌LOSS'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.RED + '==LOSS==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['P', 'V', 'B', 'P', 'P']:
              msg = '''✅G1 GREEN no ⚫🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

            elif num[0:5] == ['B', 'P', 'B', 'P', 'P']:
              msg = '''✅G1 GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              gale = 0
              return

        #===============================================================#

          elif num[0:4] == ['V', 'B', 'P', 'P']:
            if num[0:5] == ['V', 'B', 'P', 'P', 'P']:
              return

            elif num[0:4] == ['V', 'B', 'P', 'P']:
              msg = '''GALE 1'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.YELLOW + '==GALE 1==')
              print(Style.RESET_ALL)
              gale = 1
              return

          elif num[0:4] == ['P', 'B', 'P', 'P']:

            if num[0:5] == ['P', 'B', 'P', 'P', 'P']:
              return

            elif num[0:4] == ['P', 'B', 'P', 'P']:
              msg = '''✅ GREEN no ⚫🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
              return
            elif num[0:4] == ['B', 'B', 'P', 'P']:
              msg = '''✅ GREEN no ⚪🍷🗿'''
              mensagem = bot.send_message(chat_id=chat_id, text=msg)
              print(Fore.GREEN + '==WIN==')
              print(Style.RESET_ALL)
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
      print(Fore.BLUE)
      print('Porcentagem preto:', porcentagemdepretoDivididoEmFloat)
      print('Porcentagem vermelho:', porcentagemdevermelhoDivididoEmFloat)
      print(Style.RESET_ALL)
      print('Cores da rodada:', ray)
      print(Fore.YELLOW + 'FIM DA RODADA!')
      print(Style.RESET_ALL)

  except NameError as erro:
    semutilidade = 0
  except Exception as erro:
    semutilidade = 0
  #finally:
  #print('FIM.')

nav.quit()
pegaporcentagem.quit()
