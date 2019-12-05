import requests 
from bs4 import BeautifulSoup 

def info_parser(car_info):
  '''
  parse requested information for given car,
  price, model, external color, internal color, tranmission type, price and contact 
  of the car is parsed and written to a dictionary.

  Parameters: 
  car_info(bs4.element.Tag): details <div> with a class attribute of `listing-row__details`
  from cars.com
  
  Returns:
  Dictionary: a dictionary that holds concerned information 
  '''
  car_dic = {}

  # price has following form
  # <span> ${digits},{digits} </span>, where we want digits cascaded
  price = car_info.find('span', attrs={'class': 'listing-row__price'}).text 
  price = ''.join(c for c in price if c.isdigit()) # strip dollar sign and w.s.
  car_dic['price'] = price

  # year and model contained in h2 element
  # h2 is in the form
  # <h2> ${year} {brand} {model}</h2>, where we want year and model
  h2 = car_info.find('h2').text
  h2 = h2.split()

  year = h2[0] # first word is the year
  car_dic['year'] = year

  model = ' '.join(h2[2:]) # after brand take everything as model
  car_dic['model'] = model 

  # ext. color, int. color, transmission contained in ul element
  # ul has the following form
  # <li> {ext. color} <li>
  # <li> {int. color} <li>
  # <li> {transmission} <li>
  # <li> {drive train} <li>, where we only interested in first three
  ul = car_info.find('ul')
  ul_childs = ul.findChildren('li', recursive=False) 

  ext_color = ul_childs[0].text
  ext_color = ext_color.replace('Ext. Color:', '').strip() 
  car_dic['ext color'] = ext_color

  int_color = ul_childs[1].text
  int_color = int_color.replace('Int. Color:', '').strip() 
  car_dic['int color'] = int_color

  transmission = ul_childs[2].text
  transmission = transmission.replace('Transmission:', '').strip()
  car_dic['transmission'] = transmission

  # contact number is in div with class listing-row__phone
  contact = car_info.find('div', attrs={'class':'listing-row__phone'})
  # contact has few span child in it, only the last child contains number
  contact = contact.findChildren('span', recursive=False)[-1].text
  car_dic['contact'] = contact

  return car_dic

if __name__ == '__main__':
  page = requests.get("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20005&page=1&perPage=50&searchSource=GN_REFINEMENT&sort=relevance&zc=90006")

  soup = BeautifulSoup(page.content, 'html.parser')

  # div for individual car information
  car_info = soup.find('div', attrs={'class': 'listing-row__details'})
  dic = info_parser(car_info)
  print(dic)