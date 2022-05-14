import tkinter as tk
from PIL import Image, ImageTk
import csv
from operatinghours import show_operation_hours
import tkinter as tk
from PIL import Image, ImageTk
from nsfoodcourt_menulists_function import getitems, getprice
from calculatetime import calculatetimewindow
from operatinghours import show_operation_hours
import PIL


#dictionary for background image
McDonalds_background_picture = {
    'Breakfast': 'Breakfast.jpg',
    'ValueMeal': 'Value Meal.jpg',
    'Dessert': 'Dessert.jpg',
    'Sides': 'mcSides.jpg',
    'Beverages': 'Beverages.jpg'
}


#make menu into lists
def getitems_Mcdonalds(meal_name):#(Yakun & Shannon)
   with open('McDonalds_Menu.csv', mode = 'r') as csv_file:
       McDonalds_info = csv.DictReader(csv_file)
       items = []

       if meal_name == "Breakfast":
           for row in McDonalds_info:
               items.append(row ['McDonalds_Breakfast'])
           return items
       elif meal_name == 'ValueMeal':
           for row in McDonalds_info:
               items.append (row ['McDonalds_ValueMeal'])
           return items
       elif meal_name == 'Dessert':
           for row in McDonalds_info:
               items.append (row ['McDonalds_Dessert '])
           return items
       elif meal_name == 'Sides':
           for row in McDonalds_info:
               items.append (row ['McDonalds_sides'])
           return items
       elif meal_name == 'Beverages':
           for row in McDonalds_info:
               items.append (row ['McDonalds_Beverages'])
           return items
       elif meal_name == 'Breakfast_price':
           for row in McDonalds_info:
               items.append (row ['McDonalds_Breakfast_price'])
           return items
       elif meal_name == 'ValueMeal_price':
           for row in McDonalds_info:
               items.append (row ['McDonalds_ValueMeal_price'])
           return items
       elif meal_name == 'Dessert_price':
           for row in McDonalds_info:
               items.append (row ['McDonalds_Dessert_price'])
           return items
       elif meal_name == 'Sides_Price':
           for row in McDonalds_info:
               items.append (row ['McDonalds_sides_price'])
           return items
       elif meal_name == 'Beverages_price':
           for row in McDonalds_info:
               items.append (row ['McDonalds_Beverages_price'])
           return items


#function to create a window to display McDonald's Menu
def show_McDonalds_menu (meal_name,price): #(Yakun & Shannon)
    window = tk.Tk()  # create window
    window.geometry("500x500+350+70")  # size of window: window width x window height + position right + position down
    window.configure(background='white')  # colour of window background
    window.title('McDonalds') #name of the window

    #open and put in background image
    background_image = Image.open(McDonalds_background_picture[meal_name])
    background_image = ImageTk.PhotoImage(background_image, master=window)
    background_label = tk.Label(window)
    background_label.config(image = background_image)
    background_label.pack()


    #create frames to display menu labels
    mainframe = tk.Frame(window, bg='white')
    mainframe.place(relx=0.07, rely=0.445,relwidth=0.9, relheight=0.5)

    #create frames to display menu and corresponding price
    menuframe1 = tk.Frame(window, bg='white')
    menuframe1.place(relx=0.08, rely=0.51, relheight=0.45, relwidth=0.48)
    menuframe2 = tk.Frame(window, bg='white')
    menuframe2.place(relx=0.56, rely=0.51, relheight=0.45, relwidth=0.1)

    #labels for menu
    itemslabel = tk.Label(mainframe, text="Items", font=("Sitka Display", 13, 'bold', 'underline'), bg='white')
    itemslabel.place(relx=0.007, rely=0.04, relwidth=0.12, relheight=0.08)
    pricelabel = tk.Label(mainframe, text="Price", font=("Sitka Display", 13, 'bold', 'underline'), bg='white')
    pricelabel.place(relx=0.535, rely=0.04, relheight=0.08, relwidth=0.12)

    #buttons for operating hours, waiting time, and quit
    operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange', fg='white',  font=("Sitka Display", 11),relief = 'ridge', borderwidth = 1,command=lambda: show_operation_hours("McDonalds", mainframe))
    operatinghoursbutton.place(relx=0.68, rely=0.15, relheight=0.11, relwidth=0.29)
    waitingtimebutton = tk.Button(mainframe, text='Waiting Time', bg='orange', fg='white', font=("Sitka Display", 11),relief = 'ridge', borderwidth = 1,command=lambda:calculatetimewindow())
    waitingtimebutton.place(relx=0.68, rely=0.27, relheight=0.11, relwidth=0.29)
    backBtn = tk.Button(mainframe, text="<  Quit", bg='orange', fg='white',relief = 'ridge',  font=("Sitka Display", 11),borderwidth = 1, command=window.destroy)
    backBtn.place(relx=0.755, rely=0.88, relwidth=0.14, relheight=0.11)

    #insert column to display menu items
    get_Mcdonalds_list = getitems_Mcdonalds(meal_name)
    i = 4
    counter1 = 0
    for a in get_Mcdonalds_list:
        Label1 = tk.Label(menuframe1, text=get_Mcdonalds_list[counter1])
        Label1.grid(row=i, column=1, sticky='w')
        Label1.config(font=("Corbel Light", 13), bg='white')
        i += 1
        counter1 += 1

    #insert columns to display corresponding prices
    get_Mcdonalds_price_list = getitems_Mcdonalds(price)
    j = 4
    counter2 = 0
    for b in get_Mcdonalds_price_list:
        Label2 = tk.Label(menuframe2, text=get_Mcdonalds_price_list[counter2])
        Label2.grid(row=j, column=1, sticky='w')
        Label2.config(font=("Corbel Light", 13), bg='white')
        j += 1
        counter2 += 1


    window.resizable(False,False)
    window.mainloop()

