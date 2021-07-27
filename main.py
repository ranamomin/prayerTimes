
import prayerTimes
import tkinter as tk
# from tkinter import *
# from tkinter.ttk import *

city_name = ""
state_name = ""
country_name = ""
class MainApplication():

    def __init__(self, master):
        self.master = master
        self.master.title("Prayer Times")
        # self.master.iconbitmap("Blank.ico")
        
        label = tk.Label(self.master, text="Prayer Times")

        #labels


        # location_City_Input.grid(row=1, column=1, sticky="NSWE",padx=(10, 10), pady=(7.5, 0))
        
        label = tk.Label(self.master, text="Prayer Times")
        global city_label
        global state_label
        global country_label
        city_label = tk.Label(self.master, text="City", )
        state_label = tk.Label(self.master, text="State", )
        country_label = tk.Label(self.master, text="Country", )
        #input fields
        
       
        # city_n = tk.StringVar() 
        # global city_name
        global city_name
        global state_name
        global country_name

        global location_City_Input
        global location_State_Input
        global location_Country_Input

        global submit_button

        city_name = tk.StringVar()
        location_City_Input = tk.Entry(self.master,textvariable=city_name)
        # city_name = location_City_Input.get()
        
        
        state_name = tk.StringVar()
        location_State_Input = tk.Entry(self.master, textvariable=state_name)

        
        country_name = tk.StringVar()
        location_Country_Input = tk.Entry(self.master, textvariable=country_name)
        # greet_button = Button(self.master, width=25, text="Greet", command=self.greet)
        #buttons
        
        submit_button = tk.Button(self.master, width=15, text="Submit", command=self.submit_action)

        close_button = tk.Button(self.master, width=25, text="Close", command=self.closed)

        # Grid.columnconfigure(self.master, 0, weight=1)
        # Grid.rowconfigure(self.master, (0,1,2), weight=1)

        #layout
        label.grid(row=0, column=0, sticky="NSWE",padx=(10, 10), pady=(7.5, 0))
        city_label.grid(row=1, column=0, sticky="NSWE",padx=(10, 5), pady=(3, 0))
        state_label.grid(row=2, column=0, sticky="NSWE",padx=(10, 5), pady=(3, 0))
        country_label.grid(row=3, column=0, sticky="NSWE",padx=(10, 5), pady=(3, 0))

        location_City_Input.grid(row=1, column=1, sticky="NSWE",padx=(5, 10), pady=(3, 0))
        location_State_Input.grid(row=2, column=1, sticky="NSWE",padx=(5, 10), pady=(3, 0))
        location_Country_Input.grid(row=3, column=1, sticky="NSWE",padx=(5, 10), pady=(3, 0))

        submit_button.grid(row=5, column=1,sticky="NSWE", padx=(10, 10), pady=(1.5, 10))
        close_button.grid(row=6, column=1, sticky="NSWE", padx=(10, 10), pady=(1.5, 10))

        


    def submit_action(self):
      global city_name
      global state_name
      global country_name
      # print([city_name.get(),state_name.get(),country_name.get()])
      # return [city_name.get(),state_name.get(),country_name.get()]
      try:
        data = prayerTimes.prayerTimes(city_name.get(),state_name.get(),country_name.get())
      except TypeError:
        print("Type Error")
      else:
        submit_button.grid_forget()
        location_City_Input.grid_forget()
        location_State_Input.grid_forget()
        location_Country_Input.grid_forget()
        city_label.grid_forget()
        state_label.grid_forget()
        country_label.grid_forget()
        page2(data)
      # sub.configure(state='disabled')
      
      # print(city_name.get())
      # print(state_name.get())
      # print(country_name.get())
    #page two is used to display the prayer times on GUI
    


    def closed(self):
        print("Quiting")
        return self.master.destroy()
def page2(data):
      # submit_button.pack_forget()
      # print(data)
      # print("here")
      #create 9 labels for names of prayer
      prayer_label = tk.Label(root, text='')
      prayer_label.grid(row=1, column=0, pady=10)
      prayers = prayerTimes.get_prayers()
      prayers_label = ''
      for prayer in prayers:
        prayers_label = prayers_label + prayer + '\n'
        prayer_label.config(text=prayers_label)
      # print(prayerTimes.get_prayers())
      # global Fajr
      # global Sunrise
      # global Dhuhr
      # page1text.pack()
root = tk.Tk()
# root.style = Style()
#  ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# root.style.theme_use("clam")
gui = MainApplication(root)
root.mainloop()

