
import requests
import pprint
import time


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
  return return_list

def call_url(city,state,country):
  url = "http://api.aladhan.com/v1/calendarByCity?city="+city+"&state="+state+"&country="+country+"&method=2&month=04&year=2021"
  return url

def get_prayers():
  return prayers
def get_twelve_hour_format():
  return twelve_hour_format

# city = input("City: ").replace(" ","")
# state = input("State: ").replace(" ","")
# country = input("Country: ").replace(" ","")

# url = "http://api.aladhan.com/v1/calendarByCity?city=Roseville&state=California&country=United States&method=2&month=04&year=2021"




# response = requests.get(url)
# data = response.json().get('data')[0]['timings']
# pprint.pprint(response.json().get('data')[0]['timings'])

# timings=[]
# twelve_hour_format = []
# prayers = []
# for prayer in data:
#   prayers.append(prayer)
#   timings.append(data[prayer])





# #time changed to 12 hour format:

# for t in timings:
#   oneT = time.strptime(t[:5], "%H:%M")
#   timevalue_12hour = time.strftime( "%I:%M %p", oneT )
#   twelve_hour_format.append(timevalue_12hour)


# #printing prayer and time on same line
# for pray, tim in zip(prayers, twelve_hour_format):
#     print("{0}: {1}".format(pray, tim))


# import tkinter as tk

# #parent
# root = tk.Tk()
# #title
# title = tk.Label(root,text="Prayer Times")
# title.grid(row=0,column=5)
# button = tk.Button(root, text="Submit")
# button.grid(row=0,column=0)
# # lab = tk.Label(root, text="Hello World!")
# # lab.grid(row=0, column=1)

# print(prayerTimes("roseville","ca","us"))