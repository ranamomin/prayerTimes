
import requests
# import pprint
import time
import datetime
from datetime import datetime as dt


def prayerTimes(city,state,country):
  
  url = call_url(city,state,country)
  response = requests.get(url)
  data = response.json().get('data')[0]['timings']
  timings=[]
  global twelve_hour_format
  twelve_hour_format = []
  global prayers
  prayers = []
 
  for prayer in data:
    prayers.append(prayer)
    timings.append(data[prayer])
  #time changed to 12 hour format:
  
  for t in timings:
    oneT = time.strptime(t[:5], "%H:%M")
    timevalue_12hour = time.strftime( "%I:%M %p", oneT )
    twelve_hour_format.append(timevalue_12hour)
  

  #printing prayer and time on same line
  # return prayers, twelve_hour_format
  return_list = []
  for pray, tim in zip(prayers, twelve_hour_format):
      return_list.append("{0}: {1}".format(pray, tim))
  
  # return return_list
  # return get_daylight_times()

def call_url(city,state,country):
  # url = "http://api.aladhan.com/v1/calendarByCity?city="+city+"&state="+state+"&country="+country+"&method=2&month=04&year=2021&school=1&method=2"
  url1 = "http://api.aladhan.com/v1/calendarByCity?city="+city+"&state="+state+"&country="+country+"&school=2"


  return url1

def get_prayers():
  return prayers
def get_twelve_hour_format():
  return twelve_hour_format


# wrote code for daylight times if the api doesn't return correct times
def get_daylight_times():
  # mydatetime = datetime.now() # or whatever value you want
  times_only = []
  for times in twelve_hour_format:
    st = dt.strptime(times,'%I:%M %p')
    times_only.append(st)

  # return (times_only)
  new_times = []
  for times in times_only:
    nt = times + datetime.timedelta(hours=1)
    nt = nt.strftime("%r")
    new_times.append(nt)
  
  for index, t in enumerate(new_times):
    t = t[:5]+' '+t[9:]
    new_times[index] = t

  return(new_times)

# print(prayerTimes("roseville","ca","us"))