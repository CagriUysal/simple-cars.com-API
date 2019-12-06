from .cars_parser import info_parser, get_cars_info
from ..models import Car

def main():
  bmw_url = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20005&page=1&searchSource=GN_REFINEMENT&sort=relevance&zc=90006'
  ford_url = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20015&page=1&searchSource=GN_REFINEMENT&sort=relevance&zc=90006' 

  # get 50 cars information for both BMW and Ford
  print('Fetching BMW ....')
  bmw_list = get_cars_info(bmw_url, 50)
  print('Fetching Ford ....')
  ford_list = get_cars_info(ford_url, 50) 

  cars_list = bmw_list + ford_list 

  print('Writing to database ....')
  for car in cars_list:
    Car.objects.create(**car)
