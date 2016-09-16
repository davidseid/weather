# imports
import json
import urllib2
import datetime


# find date using datetime
today = datetime.datetime.today()


# website and request
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?q=PismoBeach&appid=26d344d8f5f13a5e4bc50827812b4503&units=Imperial"
forecast_data = json.load(urllib2.urlopen(forecast_url))


# check for the day
print today.day

# assigns tomorrow, which is the start of our search, if it is a single digit, add a 0
if today.day > 9:
	next_day = str(today.day + 1)
	print next_day
else:
	next_day = "0" + str(today.day + 1)

# if the month is less than 10, make sure it is written with a 0 first
if today.month < 10:
	month = "0" + str(today.month)
	print month

# creates a string of the time we will search for
the_time = "2016-" + month + "-" + next_day + " " + "18:00:00"
print the_time

# for loop, checking for the next 38 listings (which is all of them for the forecast data)
for index in range(0,38):
	
	# if the listing matches the time we are looking for
	if forecast_data['list'][index]['dt_txt'] == the_time:
	
		# print the time
		print "Found a time"
		print forecast_data['list'][index]['dt_txt']
		
		# change our time to the next day
		next_day = int(next_day) + 1
		next_day = str(next_day)
		the_time = "2016-09-" + str(next_day) + " " + "18:00:00"
		print "looking for"
		print the_time
		
		
		
		

# program will break at the end of the month, need to check if it is the next month and if so, go back and start form the beginning of the next month

