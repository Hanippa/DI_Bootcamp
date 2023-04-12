# Building a Weather App

# The current weather data can be retrieved from OpenWeatherMap using the Observation module in PyOWM (Python OpenWeatherMap).
# Use this documentation for this Mini Project.

#     Get the current weather in Tel Aviv.
#     Get current wind info of Tel Aviv.
#     Get today’s sunrise and sunset times of Tel Aviv.
#     Display all these information in a user friendly way.

#     Recreate these steps, but this time, ask the user for a location (display the information in a user friendly way).
#         Instead of working with the name of the city, retrieve the id of the city.
#         Check out the documentation section : “Identifying cities and places via city IDs”.

#     Retrieve weather forecasts : The OpenWeatherMap free tier gives you access to 5 day forecasts. The forecasts contain the weather data in three-hour intervals.
#         The methods for retrieving the forecast are:
#             forecast_at_place('Los Angeles, US', '3h')
#             forecast_at_id(5391959, '3h')
#             forecast_at_coords(lat=37.774929, lon=-122.419418, interval='3h')
#             Forecasts are useful if you want to know what the weather conditions will be throughout the day/week.

#     Use this API to retrieve the Air Pollution in a specific city.

# Mini project : XP Ninja

# BONUS: Your goal is to produce a weather GUI that shows the three-day humidity forecast for a city of your choice.
# If you’ve never built a GUI with Python, don’t worry! We’ll be going through step by step how to build it. We will be using Matplotlib to
# plot the weather data. Matplotlib uses Tkinter behind the scenes to display the interactive GUI.


# You have to reproduce this bar chart:

# You will have to use :

#     the matplotlib module for the bar chart
#     the pytz and datetime module for the date
#     the pyowm module for the weather


# Instructions:

#     Start by updating the values for the ylabel and title by creating a function called init_plot().
#     Create a function called plot_temperatures() to determine the details of the bar chart.
#     Create a function called write_humidity_on_bar_chart() to display the % humidity in the bar chart.
#     Style the bar chart
from pyowm.owm import OWM
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


owm = OWM('80202efc1b08f86c4a17a92bebaf1d4d')
mgr = owm.weather_manager()
mgr2 = owm.airpollution_manager()


location = input("WHAT IS YOUR LOCATION? : ")
observation = mgr.weather_at_place(location)
w = observation.weather


print(f"-------------------\nTHE WEATHER NOW IN {observation.location.name}\nTHE TEMPRATURE IS : {w.temperature('celsius')['temp']}\nTHE WIND SPEED IS : {w.wind()['speed']}\nTHE SUN WILL RISE AT : {datetime.utcfromtimestamp(w.srise_time)}\nAND SET AT : {datetime.utcfromtimestamp(w.sunset_time())}\nENJOY--------------")



daily_forecast = mgr.forecast_at_place(location, '3h').forecast
for weather in daily_forecast:
    print("WEATHER FOR : ",weather.reference_time('iso'), weather.status)
print(mgr2.air_quality_at_coords(32.0879267,34.7622267).air_quality_data)


humidata = {}
humidity_for = mgr.forecast_at_place(location, '3h').forecast
for weather in humidity_for:
    humidata[weather.reference_time('iso')] = weather.humidity
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 3}

plt.rc('font', **font) 

# data = {'C':20, 'C++':15, 'Java':30}
days = list(humidata.keys())
values = list(humidata.values())
  
fig = plt.figure(figsize = (20, 5))
 
plt.bar(days, values, color ='#2179b8',
        width = 0.7)

plt.xlabel("DAYS")
plt.ylabel("HUMIDITY(%)")
plt.title("HUMIDITY FORECAST")
plt.show()