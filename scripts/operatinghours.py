import tkinter as tk
import json

#function to display the operating hours when click the buttons (using JSON file) (Yakun)
def show_operation_hours (store_name, window):
   #open the JSON file that stores the information about operating hours
   with open ('operating_hours_jsonfile.json', 'r') as f:
       operating_hours = json.load(f)

       #create a window that display operating hours
       operating_hours_windows = tk.Toplevel(window, bg = '#F0C35D')
       operating_hours_windows.title("Operating Hours of " + store_name) #title of the window
       operating_hours_windows.geometry("360x180+350+70") #window dimensions


       #big title 'operating hours' to be displayed at the top part of the window page
       main_label = tk.Label(operating_hours_windows, text = 'Operating Hours',bg = '#F0C35D',font=("Berlin Sans FB Demi", 24, 'bold'),
                             fg = 'black')
       main_label.place(relx=0.15, rely=0.1)

       #to display the operating hours information
       content_label = tk.Label(operating_hours_windows, text = operating_hours[store_name],bg = '#F0C35D')
       content_label.place(relx = 0.1, rely = 0.39, relwidth = 0.8)
       content_label.config(font=("Ink Free",16))

       operating_hours_windows.resizable(False, False)
