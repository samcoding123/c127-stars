from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"
page = requests.get(START_URL)

soup = bs(page.text,'html.parser')
startable = soup.find('table')
templist = []
tablerows=startable.find_all('tr')

for i in tablerows:
    td=i.find_all('td')
    row=[j.text.rstrip() for j in td]
    templist.append(row)

starnames=[]
distance=[]
mass=[]
radius=[]
lumps=[]

for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lumps.append(templist[i][7])

df=pd.DataFrame(list(zip(starnames, distance, mass, radius, lumps)),columns=['star_name', 'distance', 'mass','radius','luminosity'])
print(df)
df.to_csv('anyname.csv')