#import modules
import requests
import json
import csv
import time


api_url = 'https://api.aviationstack.com/v1/airports'
access_key = '499313b5af90f08196e3bd55aeb22709'
limit = 100
offset = 0

airports = []
while True:

    params = {'access_key': access_key, 'limit': limit, 'offset': offset}
    
    response = requests.get(api_url, params=params)
    
    # Parse the response
    if response.status_code == 200:
        json_response = response.json()
        data = json_response['data']
        pagination = json_response['pagination']
        
        # Append the data to the master list
        airports.extend(data)
        
        # Check if we've reached the total number of records
        if pagination['count'] + pagination['offset'] >= pagination['total']:
            print(f"All {pagination['total']} records retrieved.")
            break
        
        # Increment the offset for the next call
        offset += limit
        
        # Optional: Add a delay to avoid hitting rate limits
        time.sleep(1)
    
    else:
        print(f"Error: {response.status_code}")
        break

for airport in data:
    airport_details = {
        'id': airport['id'],
        'gmt': airport['gmt'],
        'airport_id': airport['airport_id'],
        'iata_code': airport['iata_code'],
        'city_iata_code': airport['city_iata_code'],
        'icao_code': airport['icao_code'],
        'country_iso2': airport['country_iso2'],
        'geoname_id': airport['geoname_id'],
        'latitude': airport['latitude'],
        'longitude': airport['longitude'],
        'airport_name': airport['airport_name'],
        'country_name': airport['country_name'],
        'phone_number': airport['phone_number'],
        'timezone': airport['timezone']
    }
    airports.append(airport_details)


filename = '/home/ajiri/project/aviationDataAnalysis/data/raw/airport_list.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'gmt', 'airport_id', 'iata_code', 'city_iata_code', 'icao_code',
                                                 'country_iso2', 'geoname_id', 'latitude', 'longitude', 'airport_name', 
                                                 'country_name', 'phone_number', 'timezone'])
    writer.writeheader()
    writer.writerows(airports)