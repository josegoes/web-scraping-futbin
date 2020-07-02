# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:56:40 2020

@author: jose.goes
"""

import requests
import json
from bs4 import BeautifulSoup

header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
         }

proxies = {
        'HTTP':'http://81.5.103.14:8081',
        'HTTPS':'http://125.163.161:250:8080',
        }

hr = requests.get('https://www.futbin.com/20/playerPrices?player=20801&rids=50352449,67129665,100684097,134238529,117461313,151015745&_=1592956174922', headers=header)

soup = BeautifulSoup(hr.text, 'html.parser')

prices = json.loads(soup.get_text())

price_player = prices['20801']['prices']['ps']


