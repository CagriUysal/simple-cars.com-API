import requests 
from bs4 import BeautifulSoup 
import re

page = requests.get("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20005&page=1&perPage=50&searchSource=GN_REFINEMENT&sort=relevance&zc=90006")

soup = BeautifulSoup(page.content, 'html.parser')

# div for individual car information
car_info = soup.find('div', attrs={'class': 'listing-row__details'})
car_dic = {}

'''
parse requested information for each car,
following informations will be parsed from the div 
price, model, external color, internal color, transmission type, price, contact ''' 
# price has following form
# <span> ${digits},{digits} </span> where we want digits cascaded
price = car_info.find('span', attrs={'class': 'listing-row__price'}).text 
price = ''.join(re.findall(r'\d+', price)) # strip dollar sign and white spaces
car_dic['price'] = price

# year and model contained in h2 element
# h2 is in the form
# <h2> ${year} {brand} {model}</h2> where we want year and model
h2 = car_info.find('h2').text
year = re.search(r'\d+', h2).group()
model = 
print(year)
print(type(year))
