# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 00:50:16 2020

@author: Tejas
"""

import pandas as pd
import numpy as np
import ast
import re
import requests
from nltk.corpus import stopwords
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import re
import random

df_c1 = pd.read_csv('p1_StackCatalyst.csv')
df_c1['Sponsors'] = df_c1['Sponsors'].apply(lambda x: ast.literal_eval(x))



user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]



headers = {'apikey': 'AIzaSyAtrNiOay2y-tVvxDIatEWOpQmunHf0FFA', \
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit \
           537.36 (KHTML, like Gecko) Chrome", \
"Accept":"text/html,application/xhtml+xml,application/xml; \
q=0.9,image/webp,*/*;q=0.8"}

## Google API Key = AIzaSyAtrNiOay2y-tVvxDIatEWOpQmunHf0FFA  (https://developers.google.com/custom-search/v1/overview)


### A funciton to extract ticker from google search
def google(q):
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    ft = soup.find('div',class_='rc').text   ### filtered text
    sym = list(set(re.findall('\(.*?\)', ft)))
    return sym




def bloomberg(q):
    
    user_agent = random.choice(user_agent_list)
    
    headers = {'apikey': 'AIzaSyAtrNiOay2y-tVvxDIatEWOpQmunHf0FFA', \
           "User-Agent": user_agent, \
            "Accept":"text/html,application/xhtml+xml,application/xml; \
            q=0.9,image/webp,*/*;q=0.8"}
                
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('https://www.bloomberg.com/quote/'):
            aa = link['href'].split('/')[-1]
            print (aa)
            return aa
            break
    

def marketwatch(q):
 
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('https://www.marketwatch.com/investing/stock/'):
            aa = link['href'].split('/')[-1]
            print (aa)
            return aa
            break







#companyTicker = []
companyTicker1 = []
#companyTicker2 = []
for i in range(758, df_c1.shape[0]):
    
    # one row at a time    
    a = df_c1['Sponsors'].iloc[i]

    # Converting all to lower letters
    a1 = [x.lower() for x in a]  
    
    # From the remaining words, remove any non-letter punctuations
    a2 = [re.sub(r'\W+',' ', x) for x in a1]
    
    
    # Removing names with above academic words    
    academic_words = ['research', 'academic', 'university', 'school', 'college', 'center', 'institute', 'group']
    a3 = [x for x in a2 if not bool(set(academic_words) & set(x.split(' ')))]
    
    # removing stop words
    a4 = [word for word in a3 if word not in stopwords.words('english')]
    
    # for every row, find the ticker
    if (len(a4) == 0):          ### if its empty matrix
        #companyTicker.append('Academic Trials')
        companyTicker1.append('Academic Trials')
        #companyTicker2.append('Academic Trials')
        
    else:
        temp_companies = []
        temp_companies1 = []
        temp_companies2 = []
        for company in a4:
            #q = "{} 'Tickier'".format(company)
            q1 = "{} bloomberg 'Ticker'".format(company)
            #q2 = "{} marketwatch 'Ticker'".format(company)
            
            #tick = google(q)
            tick1 = bloomberg(q1)
            #tick2 = marketwatch(q2)
            #temp_companies.append(tick)
            temp_companies1.append(tick1)
            #temp_companies2.append(tick2)
            
        #companyTicker.append(temp_companies)
        companyTicker1.append(temp_companies1)
        #companyTicker2.append(temp_companies2)

    if (i%100 ==0):
        print(i)


#companyTicker = [str(x).replace('[','').replace(']','').replace(',', '') for x in companyTicker]
companyTicker1 = [str(x).replace('[','').replace(']','').replace(',', '') for x in companyTicker1]
#companyTicker2 = [str(x).replace('[','').replace(']','').replace(',', '') for x in companyTicker2]



comb = pd.DataFrame()
comb['Google'] = companyTicker
comb['Bloomberg'] = companyTicker1
comb['MarketWatch'] = companyTicker2

df_sample = df_c1.head(431)

df_sample.reset_index(drop = True, inplace = True)
comb.reset_index(drop = True, inplace = True)
df_final = pd.concat([df_sample, comb], 1)

df_final.to_csv('WithtickersSample.csv', index = False)










df_p1 = pd.read_csv('p1_StackCatalyst.csv')

a = ast.literal_eval(df_p1['Sponsors'].iloc[34])

# Converting all to lower letters
a1 = [x.lower() for x in a]  

# From the remaining words, remove any non-letter punctuations
a2 = [re.sub(r'\W+',' ', x) for x in a1]


academic_words = ['research', 'academic', 'university', 'school', 'college', 'center', 'institute', 'group']
# Removing names with above academic words
a3 = [x for x in a2 if not bool(set(academic_words) & set(x.split(' ')))]

# ...
a4 = [word for word in a3 if word not in stopwords.words('english')]

companyRecognized = []
companyTicker = []
url = 'https://financialmodelingprep.com/api/v3/search?query={}&limit=10&exchange=Nasdaq'.format('seattle genetics')
info = requests.get(url).json()
companyRecognized.append(info['name'])
companyTicker.append(info['symbol']) 






import requests
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit \
           537.36 (KHTML, like Gecko) Chrome", \
"Accept":"text/html,application/xhtml+xml,application/xml; \
q=0.9,image/webp,*/*;q=0.8"}

def google(q):
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    soup.find('div',class_='rc').text
       
q = google("Tejas Ticker")
q = google("Hi")



q = "abbvie marketwatch 'Ticker'"
q = '+'.join(q.split())
url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')

for link in soup.find_all('a', href=True):
    if link['href'].startswith('https://www.marketwatch.com/investing/stock/'):
        aa = link['href'].split('/')[-1]
        print (aa)
        break


bloomberg('google')



from bs4 import BeautifulSoup
import json

url = "https://www.us-proxy.org/"
r = requests.get(url)

soup = BeautifulSoup(r.text)
soup.find_all('td')

a = list(soup.find_all('td', class_ = 'hx'))

ii = []
for i in range(0, len(a)):
    if 'yes' in a[i]:
        ii.append(i)




iplist = []
a1 = list(soup.find_all('td'))
a1 = [str(x) for x in a1]

for i in range(0, len(a1)):
    if '.' in a1[i]:
        iplist.append(a1[i])


iplist = [x.replace('<td>','').replace('</td>', '') for x in iplist]


yesIp = []
for i in range(0, len(ii)):
    yesIp.append(iplist[ii[i]])































