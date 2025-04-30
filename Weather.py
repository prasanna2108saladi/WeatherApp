import requests
import os
from datetime import datetime

user_api="6e37e6a33299da36f75c735eed0607af"
location=input("Enter City Name :   ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link=requests.get(complete_api_link)
api_data=api_link.json()

if api_data['cod']=='404':
  print("Invalid City:{}, Please enter the correct City name".format(location))
else:
  temp_city = ((api_data['main']['temp']) - 273.15)
  weather_desc=api_data['weather'][0]['description']
  humidity=api_data['main']['humidity']
  wind_speed=api_data['wind']['speed']
  date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

  print("========================================================")
  print("Weather Status for - {} || {}".format(location.upper(),date_time))
  print("========================================================")

  print("Current Tenperatur is : {:.2f} deg C".format(temp_city))
  print("Current Weather is :",weather_desc)
  print("Current Humidity :",humidity, '%')
  print("Current Wind Speed :",wind_speed,'kmph')

