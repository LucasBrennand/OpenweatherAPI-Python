import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
print(API_KEY)
if API_KEY is None:
    raise ValueError("API key not found!")
URL = ''

city_input = input("Digite uma cidade que você quer procurar o clima: ")

def get_lat_and_long():
    lat_and_lon = []
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_input}&limit={1}&appid={API_KEY}")
        response.raise_for_status()
        data = response.json()
        for i in data:
            lat_and_lon.append(i["lat"])
            lat_and_lon.append(i["lon"])
        # print(lat_and_lon)
        return lat_and_lon
        
    except requests.exceptions.RequestException as e:
        print("Error:",e)

async def get_weather(lat_and_lon):
    try:
    

get_lat_and_long()

# try:
#     response = requests.get(URL)
#     response.raise_for_status()
#     data = response.json()
#     for i in data:
#         for j in range(6):
#             print(j["title"])
            
# except requests.exceptions.RequestException as e:
#     print(e)