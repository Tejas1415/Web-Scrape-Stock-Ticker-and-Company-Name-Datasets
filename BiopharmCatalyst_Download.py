# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:00:49 2020

@author: Tejas

Stealing BioPharamCatalyst data :P 

Step 1: Go to https://www.biopharmcatalyst.com/calendars/historical-catalyst-calendar
Step 2: Right click, and go to view source HTML. 
Step 3: Copy the whole data and paste it in a notepad file and name it "CatalystHistory.txt"
Step 4: Just run the below code and enjoy :P 

"""

#### Read their whole view-source html file.
f=open('catalysthistory.txt', encoding="utf8")
x = f.readlines()



#### Now, start with this string and then record each element.
#check if line contains = "https://www.biopharmcatalyst.com/company"
import re
check_string = 'https://www.biopharmcatalyst.com/company'

#### Start all the variables we want to record
ticker = []
drug = []
indication = []
AppCRL = []
Cdate = []
Cdescription = []

for i in range(0, len(x)):
    
    if check_string in x[i]:
        #try:
        
        #Ticker
        start = "\"ticker\">" 
        end = '</'
        ticker.append(re.search('%s(.*)%s' % (start, end), x[i]).group(1)[:-4])
        
        
        #Drug Name
        start = "\"drug\">"
        end = '</'
        drug.append(re.search('%s(.*)%s' % (start, end), x[i+2]).group(1))
        
        
        #Indication
        start = "\"indication\">"
        end = '</div>'
        indication.append(re.search('%s(.*)%s' % (start, end), x[i+3]).group(1))
        
        
        #Approved or CRL 
        start = " "
        end = '\n'
        AppCRL.append(re.search('%s(.*)%s' % (start, end), x[i+7]).group(1))
        
        try:
            #Catalyst Date
            start = " \">"
            end = '</time>'
            Cdate.append(re.search('%s(.*)%s' % (start, end), x[i+21]).group(1))
            
            
            #Catalyst Description
            start = "-note\">"
            end = '</div>'
            Cdescription.append(re.search('%s(.*)%s' % (start, end), x[i+23]).group(1))
        
        except:
             #Catalyst Date
            start = " \">"
            end = '</time>'
            Cdate.append(re.search('%s(.*)%s' % (start, end), x[i+20]).group(1))
            
            
            #Catalyst Description
            start = "-note\">"
            end = '</div>'
            Cdescription.append(re.search('%s(.*)%s' % (start, end), x[i+22]).group(1))
            
            
            
            

import pandas as pd

final = pd.DataFrame()
final['Ticker'] = ticker
final['Drug Name'] = drug
final['Indication'] = indication
final['Approved or CRL'] = AppCRL
final['Catalyst Date'] = Cdate
final['Catalyst Description'] = Cdescription

final.to_csv('BioPharmCatalyst.csv', index = False)


















