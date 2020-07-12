# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:15:04 2020

@author: jose.goes
"""

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import time
import os

list_name = []
   

for l in range(2)[1:]:
    
    url = requests.get('https://www.futbin.com/20/players?page='+str(l))
    print('Página: '+str(l)+' Cod. Status: '+str(url.status_code))
    
    if url.status_code == 200:
        
        try:
            
            soup = BeautifulSoup(url.text, 'html.parser')
            
            for i in range(30):
                list_name.append(soup.find_all('a', {'class':'player_name_players_table'})[i].get('href'))
                
            print('Página: '+str(l)+' Raspagem: '+'Finalizada')
        except:
            print('Página: '+str(l)+' Raspagem: '+'Não Finalizada')
    
        time.sleep(0.5)
    
    elif url.status_code == 429:
        
        print('Página: '+str(l)+' Raspagem: '+'Fazendo nova tentativa em 0.5s')
        
        time.sleep(0.5)
        
dfPlayers = pd.DataFrame(data={'Jogadores':list_name})

dfConsolidado = pd.DataFrame()

for i in range(len(dfPlayers)):
    result_split = pd.DataFrame(data={'null':[dfPlayers['Jogadores'][i].split('/')[0]],
                                      'Temporada FIFA':[dfPlayers['Jogadores'][i].split('/')[1]],
                                      'Tipo':[dfPlayers['Jogadores'][i].split('/')[2]],
                                      'ID Player':[dfPlayers['Jogadores'][i].split('/')[3]],
                                      'Nome Jogador':[dfPlayers['Jogadores'][i].split('/')[4]]})
    dfConsolidado = pd.concat([dfConsolidado, result_split], sort=False)

cur_dir = os.getcwd()

dfConsolidado.to_excel(cur_dir+'\Output\dfConsolidado.xlsx', index=False)