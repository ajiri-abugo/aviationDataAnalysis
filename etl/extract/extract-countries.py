import pandas as pd
from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.geonames.org/countries/'
json_path = '/home/ajiri/project/aviationDataAnalysis/data/raw/countries.json'
page = requests.get(url).text
data = BeautifulSoup(page,'html.parser')
table_attribs = ['ISO_3166_alpha2', 'ISO_3166_alpha3', 'ISO_3166_numeric', 'fips', 'Country', 'Capital', 'Area in km2', 'Population', 'Continent']
df = pd.DataFrame(columns=table_attribs)
tables = data.find_all('table')
tgt_table = tables[1]

rows = tgt_table.find_all('tr')[1:]

for row in rows:
    count = 0
    col = row.find_all('td')
    if len(col)==9:
        data_dict = {"ISO_3166_alpha2": col[0].text.strip(),
                     "ISO_3166_alpha3": col[1].text.strip(),
                     "ISO_3166_numeric": col[2].text.strip(),
                     "fips": col[3].text.strip(),
                     "Country": col[4].a.text.strip(),
                     "Capital": col[5].text.strip(),
                     "Area in km2": col[6].text.strip(),
                     "Population": col[7].text.strip(),
                     "Continent": col[8].text.strip()
                    }
        df1 = pd.DataFrame(data_dict, index=[0])
        df1['Area in km2'] = df1['Area in km2'].astype(str)
        df1['Population'] = df1['Population'].astype(str)
        df1['Area in km2'] = df1['Area in km2'].str.replace(',','').str.replace('"','')
        df1['Population'] = df1['Population'].str.replace(',','').str.replace('"','')
        df = pd.concat([df,df1], ignore_index=True)
        count+=1
    else:
        break

df.to_json(json_path, orient='records', lines=True)
