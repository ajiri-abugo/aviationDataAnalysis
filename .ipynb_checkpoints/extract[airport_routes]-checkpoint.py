#airport iata code list
#import modules
from pandas import *
 
# reading CSV file
data = read_csv(filename)
 
# converting column data to list
airport_iata_codes = data['iata_code'].tolist()

