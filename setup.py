from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time
import telegram
import os
import colorama
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
init()

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)
#dados = webdriver.Chrome(options = chrome_options)

token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
chat_id = '-1001896645285'
bot = telegram.Bot(token)

nav.get('https://blaze.com/pt/games/double')
#dados.get('https://tipminer.com/blaze/double')

os.system('cls') or None

print(Fore.GREEN + 'BOT INICIADO!')
print(Style.RESET_ALL)
foradogiro = 0

while True:

    def qualnum(x):
        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14

        if x == '0':
            return 0

    def qualcor(x):
        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'

        if x == '0':
            return 'Branco'



    try:
        resulROOL = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
        pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
        #dadosV = dados.find_element(By.XPATH , '//*[@class="card-body pb-2"]').text

    except NameError as erro:
        print(Fore.GREEN + 'Ocorreu um erro de codigo "403" mas o bot está reiniciando!')
        print(Style.RESET_ALL)
    except Exception as erro:
        print(Fore.RED + 'Ocorreu um erro de codigo "404" mas o bot está reiniciando!')
        print(Style.RESET_ALL)


    tfg = pegardados.split()

    pd = tfg[0:16]

    mapeando = map(qualnum, pd)
    mapeando2 = map(qualcor, pd)

    finalnum = list(mapeando)
    finalcor = list(mapeando2)

    c = nav.page_source
    soup = BeautifulSoup(c, 'html.parser')
    go = soup.find('div', class_="entries main")
    for i in go:
        if i.getText():
            tfg.append(i.getText())
        else:
            tfg.append('0')



    if resulROOL == 'Girando...':
        print('Analisando...')
        foradogiro = 1

    if foradogiro == 1 and resulROOL != 'Girando...':

        #Mostra as cores que caiu no Giro
        print(Fore.BLUE)
        print(finalcor)
        print(Style.RESET_ALL)

        print(Fore.YELLOW + 'Fim da rodada!')
        print(Style.RESET_ALL)

        def check(num):

        #==================================================Estrategia Teste============================================#
            if num[0:3] == ['P', 'P', 'P']:

                if num[0:4] == ['P', 'P', 'P', 'P']:
                    return

                elif num[0:3] == ['P', 'P', 'P']:
                    msg = '''✅ GREEN no ⚫🍷🗿'''
                    mensagem = bot.send_message(chat_id=chat_id, text=msg)
                    return




            if num[0:3] == ['V', 'P', 'P']:

                if num[0:4] == ['V', 'P', 'P', 'P']:
                    return

                elif num[0:3] == ['V', 'P', 'P']:
                    msg = '''❌LOSS'''
                    mensagem = bot.send_message(chat_id=chat_id, text=msg)
                    return





            if num[0:2] == ['P', 'P']:

                if num[0:2] == ['P', 'P', 'P']:
                    return
                
                elif num[0:2] == ['P', 'P']:
                    msg = '''🚨Entrada confirmada🚨
    📌Entrar no ⚫ 
    🛡️Proteger o ⚪'''
                    mensagem = bot.send_message(chat_id=chat_id, text=msg)
                    return
                



            if num[0:1] == ['P']:

                if num[0:2] == ['P', 'P']:
                    return
                
                elif num[0:1] == ['P']:
                    msg = '''⚠️ATENÇÃO⚠️
    Possivel entrada no ⚫ 
    ⏰Aguarde o sinal...'''
                    mensagem = bot.send_message(chat_id=chat_id, text=msg)
                    if resulROOL == 'Girando...':
                        mensagem.delete()
                    return


        #==================================================FIM============================================#
        checkversion = check(finalcor)
        time.sleep(1)
        foradogiro = 0
