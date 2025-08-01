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
        print()
        response.raise_for_status()
        data = response.json()
        for i in data:
            lat_and_lon.append(i["lat"])
            lat_and_lon.append(i["lon"])
        # print(lat_and_lon)
        return lat_and_lon
        
    except requests.exceptions.RequestException as e:
        print("Error:",e)

def get_weather(lat_and_lon):
    lat, lon = lat_and_lon
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        )
        response.raise_for_status()
        data = response.json()

        temp_celsius = data["main"]["temp"] - 273.15
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"""
        Clima em {city_input}:
        🌡 Temperatura: {temp_celsius:.1f}°C
        🌥 Descrição: {description}
        💧 Umidade: {humidity}%
        """)
    except requests.exceptions.RequestException as e:
        print("Erro:", e)

get_weather(get_lat_and_long())

# try:
#     response = requests.get(URL)
#     response.raise_for_status()
#     data = response.json()
#     for i in data:
#         for j in range(6):
#             print(j["title"])
            
# except requests.exceptions.RequestException as e:
#     print(e)