# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:17:48 2020

@author: Tejas
"""


#### Downloading Tickers from NASDAQ
import datapackage

import pandas as pd

data_url = 'https://datahub.io/core/nyse-other-listings/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
        print (data)


data.to_csv('Nasdaq_company_ticker.csv', index = False)





########### Getting company name for given symbols for all stocks in NYSE
df = pd.read_csv('NYSE_stocktickers.csv')

tickersList = df['ticker'].to_list()


import yfinance as yf

tickerName = []
companyName = []
for i in range(len(tickersList)):
    
    tick = yf.Ticker(tickersList[i])
    try:
        companyName.append(tick.info['longName'])
        tickerName.append(tickersList[i])
    except:
        pass
    
    if (i % 200 == 0):
        print (i)

NYSE = pd.DataFrame()
NYSE['StockTickers'] = tickerName
NYSE['CompanyName'] = companyName
NYSE.to_csv('NYSE_stock_tickers.csv', index = False)






############### American Stock Exchange ##############

df2 = pd.read_csv('AMEX.csv')
df2.columns




import requests


from fuzzywuzzy import process

def getCompany(text):
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    stockList = r.json()
    return process.extractOne(text, stockList)[0]



def get_symbol(symbol):
   # url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    url = "http://finance.yahoo.com/d/quotes.csv?s=amd&f=nb4t8"
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


tickersList = df2['<ticker>'].to_list()

tickerName = []
companyName = []
for i in range(len(tickersList)):
    
    try:
        companyName.append(getCompany(tickersList[i]))
        tickerName.append(tickersList[i])
    except:
        pass
    
    if (i % 200 == 0):
        print (i)


AMEX = pd.DataFrame()
AMEX['StockTickers'] = tickerName
AMEX['CompanyName'] = companyName
pd.read_json(companyName)
AMEX.to_csv('AMEX_stock_tickers.csv', index = False)






getCompany('GOOG')['name']
getCompany('Alphabet')



























