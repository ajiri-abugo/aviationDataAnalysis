import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.geonames.org/countries/'
csv_path = '/home/ajiri/project/aviationDataAnalysis/data/raw/countries.csv'
page = requests.get(url).text
data = BeautifulSoup(page,'html.parser')
table_attribs = ['ISO-3166-alpha2', 'ISO-3166-alpha3', 'ISO-3166-numeric', 'fips', 'Country', 'Capital', 'Area in km^2', 'Population', 'Continent']
df = pd.DataFrame(columns=table_attribs)
tables = data.find_all('table')
print(len(tables))
tgt_table = tables[1]

rows = tgt_table.find_all('tr')[1:]

for row in rows:
    count = 0
    col = row.find_all('td')
    if len(col)==9:
        data_dict = {"ISO-3166-alpha2": col[0].text,
                     "ISO-3166-alpha3": col[1].contents[0],
                     "ISO-3166-numeric": col[2].contents[0],
                     "fips": col[3].text,
                     "Country": col[4].a.contents[0],
                     "Capital": col[5].text,
                     "Area in km^2": col[6].contents[0],
                     "Population": col[7].contents[0],
                     "Continent": col[8].contents[0]
                    }
        df1 = pd.DataFrame(data_dict, index=[0])
        df = pd.concat([df,df1], ignore_index=True)
        count+=1
    else:
        break

print(df)

df.to_csv(csv_path, index=False)