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

from webdriver_manager.chrome import ChromeDriverManager

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
gDriver = webdriver.Chrome(
    chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)
gDriver.get("https://www.python.org/")
time.sleep(3)
gDriver.save_screenshot("my_screenshot.png")
gDriver.close()

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)

token = '5744690430:AAHdhSKGoDml-c-6jDoAXsTZrZ7py-uVryU'
chat_id = '-1001896645285'
bot = telegram.Bot(token)

nav.get('https://blaze.com/pt/games/double')

foradogiro = 0



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
        print('Ocorreu um erro de codigo "403" mas o bot está reiniciando!')
    except Exception as erro:
        print('Ocorreu um erro de codigo "404" mas o bot está reiniciando!')

    if resulROOL == 'Girando...':
        foradogiro = 1



    if foradogiro == 1 and resulROOL != 'Girando...':

	    def resultado(num):

	        if num[0:4] == ['P', 'V', 'V', 'V']:

	            msg = '''✅ GREEN no ⚫'''
	            mensagem = bot.send_message(chat_id=chat_id, text=msg)

	        elif num[0:4] == ['V', 'V', 'V', 'V']:

	            text = '''✅ LOSS'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)

	        elif num[0:3] == ['V', 'V', 'V']:

	            text = '''✅ Entrada confirmada, entrar no ⚫
	                      Buscar apoio no ⚪'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)

	        elif num[0:2] == ['V', 'V']:

	            text = '''✅ Possivel entrada no ⚫
	                Buscar apoio no ⚪'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)






	        elif num[0:4] == ['V', 'P', 'P', 'P']:

	            text = '''✅ GREEN no 🔴'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)

	        elif num[0:4] == ['P', 'P', 'P', 'P']:

	            text = '''✅ LOSS'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)

	        elif num[0:3] == ['P', 'P', 'P']:

	            text = '''✅ Entrada confirmada, entrar no 🔴
	                   Buscar apoio no ⚪'''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)

	        elif num[0:2] == ['P', 'P']:

	            text = '''✅ Possivel entrada no 🔴
	                 Buscar apoio no ⚪ '''
	            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
	            results = requests.get(url_base)
	        print(num)
	    foradogiro = 0
	    resultado(ray)
