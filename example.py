# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:28:37 2018

@author: keovkevin
"""
#import the library used to query a website
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
# specify the url
quote_page = urllib.request.Request('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India') 
# query the website and return the html to the variable page
page = urllib.request.urlopen(quote_page)
#import the Beautiful soup functions to parse the data returned from the website
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "lxml")
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#import pandas to convert list to data frame

df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print (df)
