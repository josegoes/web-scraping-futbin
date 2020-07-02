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

list_name = []
   

for l in range(756)[1:]:
    
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

dfPlayers.to_excel(r'c:\users\jose.goes\desktop\dfPlayers.xlsx', index=False)