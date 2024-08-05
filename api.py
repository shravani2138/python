URL :https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=metric

API key :9aee160dfc24543bd7360aa4efb95945

import json
import requests
#API to fetch temperature of city
city_name = input("enter city name :")
api_keys='9aee160dfc24543bd7360aa4efb95945'
#To build URL api
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_keys}&units=metric'
get_server_information=requests.get(api_url)
print(get_server_information.json())