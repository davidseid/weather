#!/usr/bin/env python
# author: David Seidenberg
# project: What's the weather? 
# source: Reddit beginner projects

# project description
'''
Background
If you would like to know the basics of what an API is, check out this post by iamapizza. 
http://www.reddit.com/r/explainlikeimfive/comments/qowts/eli5_what_is_api/c3z9kok

Goal
Create a program that pulls data from OpenWeatherMap.org that prints out information about 
the current weather, such as the high, the low, and the amount of rain for wherever you live. 
Depending on how skilled you are, you can actually do some neat stuff with this project.

Subgoals
Print out data for the next 5-7 days so you have a 5 day/week long forecast.
Print the data to another file that you can open up and view at, instead of viewing the 
information in the command line.

If you know html, write a file that you can print information to so that your project is
more interesting. Here is an example of the results from what I threw together.

Tips
APIs that are in Json are essentially lists and dictionaries. Remember that to reference 
something in a list, you must refer to it by what number element it is in the list, and to 
reference a key in a dictionary, you must refer to it by it's name.
Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your 
data in Fahrenheit.
'''

# imports
import json
import urllib2
import time

intro = "\nThis program will tell you the weather for today and the forecast for the next 5 days."
print intro

f = open('weather.txt', 'w')


today_url = "http://api.openweathermap.org/data/2.5/weather?q=PismoBeach&appid=26d344d8f5f13a5e4bc50827812b4503&units=Imperial"
today_data = json.load(urllib2.urlopen(today_url))

low = today_data['main']['temp_min']
high = today_data['main']['temp_max']

today_msg = "\nToday's low is %s and the high is %s." % (low, high)

print today_msg,
f.write(today_msg)

try:
	rain = today_data['rain']
	rain_msg = "\nThe rain forecast is: %s\n" % (rain)

except KeyError:
	rain_msg = "No rain!\n"

print rain_msg
f.write(rain_msg)
	
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?q=PismoBeach&appid=26d344d8f5f13a5e4bc50827812b4503&units=Imperial"
forecast_data = json.load(urllib2.urlopen(forecast_url))

days_ahead = 0
index = 0

while days_ahead < 4:
	date_time = forecast_data['list'][index]['dt_txt']
	low = forecast_data['list'][index]['main']['temp_min']
	high = forecast_data['list'][index]['main']['temp_max']
	weather_msg = "\nAccording to the forecast for %s, the temperature will be approximately %s." % (date_time, high)
	print weather_msg
	f.write(weather_msg)
	index += 8
	days_ahead += 1

#TASKS
#See if I can fix the index thing so that I can specifically just pull the same time each day directly, without having to add hours
#Try to create an html file that works with this info so that i can visualize it in a cool way

