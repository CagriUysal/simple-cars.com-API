from .cars_parser import info_parser, get_cars_info
from ..models import Car

def main():
  
  cars_config = {
    'bmw': 20005,
    'ford': 20015
  }
  
  cars_list = []
  for car_name, car_id in cars_config.items():
    url = f'https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId={car_id}&page=1&searchSource=GN_REFINEMENT&sort=relevance&zc=90006'
    print(f'Fething {car_name})
    cars_list.append(get_cars_info(url, 50))

  print('Writing to database ....')
  for car in cars_list:
    Car.objects.create(**car)
