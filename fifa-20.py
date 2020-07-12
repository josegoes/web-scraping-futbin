# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:56:40 2020

@author: jose.goes
"""

import requests
import json
from bs4 import BeautifulSoup
import os
import pandas as pd

def search_player(name_player, id_player):

        header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }

        hr = requests.get('''https://www.futbin.com/20/player/{}/{}'''.format(id_player, name_player), headers=header)

        soup = BeautifulSoup(hr.text, 'html.parser')
        
        player = soup.find_all('div', {'id':'page-info'})[0].get('data-player-resource')
        
        return player

player = search_player('lionel-messi', 44079)



def search_price(id_player):

        header = {
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                }

        proxies = {
                'HTTP':'http://81.5.103.14:8081',
                'HTTPS':'http://125.163.161:250:8080',
                }

        hr = requests.get('''https://www.futbin.com/20/playerPrices?player={}'''.format(id_player), headers=header)

        soup = BeautifulSoup(hr.text, 'html.parser')

        prices = json.loads(soup.get_text())

        price_player = prices[id_player]['prices']['ps']

        dfPrice = pd.DataFrame(data={'Preço':[price_player['LCPrice']]})

        cur_dir = os.getcwd()

        dfPrice.to_excel(cur_dir+'\Output\dfPrice.xlsx', index=False)

search_price(player)
