#!/usr/bin/env python
# author: David Seidenberg
# project: What's the weather? 
# source: Reddit beginner projects

# description/goals
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
import datetime

# intro msg
intro = "\nThis program will tell you the weather for today and the forecast for the next 5 days."
print intro

# opens text file to be written to
f = open('weather.txt', 'w')

# url for today at pismo beach using owm api
today_url = "http://api.openweathermap.org/data/2.5/weather?q=PismoBeach&appid=26d344d8f5f13a5e4bc50827812b4503&units=Imperial"

# loads json data
today_data = json.load(urllib2.urlopen(today_url))

# todays low and high printing and writing
low = today_data['main']['temp_min']
high = today_data['main']['temp_max']
today_msg = "\nToday's low is %s and the high is %s." % (low, high)
print today_msg,
f.write(today_msg)


# checks for rain and displays
try:
	rain = today_data['rain']
	rain_msg = "\nThe rain forecast is: %s\n" % (rain)
except KeyError:
	rain_msg = "No rain!\n"
print rain_msg
f.write(rain_msg)


# find today's date
today = datetime.datetime.today()



# start forecast at tomorrow (adjust for digits)
if today.day > 9:
	next_day = str(today.day + 1)
else:
	next_day = "0" + str(today.day + 1)
	


# if the month is less than 10, makes sure it is written with a 0 first
if today.month < 10:
	month = "0" + str(today.month)
	


# creates a string of the time we will search for
the_time = "2016-" + month + "-" + next_day + " " + "18:00:00"



# url and json load for pismo beach forecast
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?q=PismoBeach&appid=26d344d8f5f13a5e4bc50827812b4503&units=Imperial"
forecast_data = json.load(urllib2.urlopen(forecast_url))


# loops through the next 38 listings (which is all of the forecast data)
for index in range(0,38):

# if the listing matches the time we are looking for
	if forecast_data['list'][index]['dt_txt'] == the_time:
		
		# prints out and writes everything we need
		low = forecast_data['list'][index]['main']['temp_min']
		high = forecast_data['list'][index]['main']['temp_max']
		date = the_time[:-9]
		weather_msg = "\nAccording to the forecast for %s, the temperature will be approximately %s." % (date, high)
		print weather_msg
		f.write(weather_msg)
	
		# change our time to the next day
		next_day = int(next_day) + 1
		next_day = str(next_day)
		the_time = "2016-09-" + str(next_day) + " " + "18:00:00"
		
		

# WHAT TO FIX		
# program will break at the end of the month, need to check if it is the next month and if so, go back and start form the beginning of the next month

# GOALS
#Try to create an html file that works with this info so that i can visualize it in a cool way
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help