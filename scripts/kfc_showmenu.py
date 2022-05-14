import csv
import tkinter as tk
from PIL import Image, ImageTk
from calculatetime import calculatetimewindow
from operatinghours import show_operation_hours

#Dictinoary to store the background pictures for KFC menus 
KFC_background_picture = {
    'HotDeals': 'Hot Deals.jpg',
    'Boxes': 'Boxes.jpg',
    'Chicken': 'Chicken (A La Carte).jpg',
    'Bowls': 'Bowl (A La Carte).jpg',
    'BowlMeals': 'Bowl Meals.jpg',
    'Burger': 'Burgers.jpg',
    'BurgerMeals': 'Burger Meals.jpg',
    'sharing5': 'Sharing 5.jpg',
    'sharing24': 'Sharing 24.jpg',
    'sides': 'Sides.jpg',
    'drinks':'Drinks.jpg',
    'ChickenMeals': 'Chicken Meals.jpg'
}


#Function to make menu into lists
def getitems_kfc_menu(meal_name):#(Yakun & Shannon)
   with open('kfc_menu.csv', mode = 'r') as csv_file:
       kfc_info = csv.DictReader(csv_file)
       items = []

       if meal_name == "HotDeals":
           for row in kfc_info:
               items.append(row ['item_hotdeals'])
           return items
       elif meal_name == 'ChickenMeals':
           for row in kfc_info:
               items.append (row ['item_mchicken'])
           return items
       elif meal_name == 'BurgerMeals':
           for row in kfc_info:
               items.append (row ['item_mburger'])
           return items
       elif meal_name == 'Boxes':
           for row in kfc_info:
               items.append (row ['item_boxes'])
           return items
       elif meal_name == 'BowlMeals':
           for row in kfc_info:
               items.append (row ['item_mbowls'])
           return items
       elif meal_name == 'sharing24':
           for row in kfc_info:
               items.append (row ['item_sharing24'])
           return items
       elif meal_name == 'sharing5':
           for row in kfc_info:
               items.append (row ['item_sharing5'])
           return items
       elif meal_name == 'Burger':
           for row in kfc_info:
               items.append (row ['item_aburger'])
           return items
       elif meal_name == 'Chicken':
           for row in kfc_info:
               items.append (row ['item_achicken'])
           return items
       elif meal_name == 'Bowls':
           for row in kfc_info:
               items.append (row ['item_abowl'])
           return items
       elif meal_name == 'sides':
           for row in kfc_info:
               items.append (row ['item_sides'])
           return items
       elif meal_name == 'drinks':
           for row in kfc_info:
               items.append (row ['item_drinks'])
           return items

#function to make price of the menu into lists 
def getitems_kfc_price(meal_name):#(Yakun & Shannon)
   with open('kfc_menu.csv', mode = 'r') as csv_file:
       kfc_info = csv.DictReader(csv_file)
       items = []

       if meal_name == "HotDeals":
           for row in kfc_info:
               items.append(row ['price_hotdeals'])
           return items
       elif meal_name == 'ChickenMeals':
           for row in kfc_info:
               items.append (row ['price_mchicken'])
           return items
       elif meal_name == 'BurgerMeals':
           for row in kfc_info:
               items.append (row ['price_mburger'])
           return items
       elif meal_name == 'Boxes':
           for row in kfc_info:
               items.append (row ['price_boxes'])
           return items
       elif meal_name == 'BowlMeals':
           for row in kfc_info:
               items.append (row ['price_mbowls'])
           return items
       elif meal_name == 'sharing24':
           for row in kfc_info:
               items.append (row ['price_sharing24'])
           return items
       elif meal_name == 'sharing5':
           for row in kfc_info:
               items.append (row ['price_sharing5'])
           return items
       elif meal_name == 'Burger':
           for row in kfc_info:
               items.append (row ['price_aburger'])
           return items
       elif meal_name == 'Chicken':
           for row in kfc_info:
               items.append (row ['price_achicken'])
           return items
       elif meal_name == 'Bowls':
           for row in kfc_info:
               items.append (row ['price_abowl'])
           return items
       elif meal_name == 'sides':
           for row in kfc_info:
               items.append (row ['price_sides'])
           return items
       elif meal_name == 'drinks':
           for row in kfc_info:
               items.append (row ['price_drinks'])
           return items


#Function to create window for KFC's menu
def show_kfc_menu (meal_name):#(Yakun & Shannon)
    window = tk.Tk()  # create window
    window.geometry("500x500+350+70")  # size of window: window width x window height + position right + position down
    window.configure(background='white')  # colour of window background
    window.title('KFC')

    #open and put in the backgournd image
    background_image = Image.open(KFC_background_picture[meal_name])
    background_image = ImageTk.PhotoImage(background_image, master=window)
    background_label = tk.Label(window)
    background_label.config(image = background_image)
    background_label.pack()

    #frames to display menu information
    mainframe = tk.Frame(window, bg='white')
    mainframe.place(relx=0.07, rely=0.43,relwidth=0.9, relheight=0.5)
    menuframe1 = tk.Frame(window, bg='white')
    menuframe1.place(relx=0.09, rely=0.48, relheight=0.45, relwidth=0.48)
    menuframe2 = tk.Frame(window, bg='white')
    menuframe2.place(relx=0.56, rely=0.48, relheight=0.45, relwidth=0.1)

    #create buttons for operating hours, waiting time, and quit
    operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange',fg='white',  font=("Sitka Display", 11),
                                     relief = 'ridge', borderwidth = 1,command=lambda: show_operation_hours("KFC", mainframe))
    operatinghoursbutton.place(relx=0.7, rely=0.12, relheight=0.11, relwidth=0.27)
    waitingtimebutton = tk.Button(mainframe, text='Waiting Time', bg='orange',  fg='white',
                                  font=("Sitka Display", 11),relief = 'ridge', borderwidth = 1,command=lambda:calculatetimewindow())
    waitingtimebutton.place(relx=0.7, rely=0.25, relheight=0.11, relwidth=0.27)
    backBtn = tk.Button(mainframe, text="< Quit", bg='orange',
                        fg='white',relief = 'ridge',  font=("Sitka Display", 11),borderwidth = 1, command=window.destroy)
    backBtn.place(relx=0.755, rely=0.88, relwidth=0.14, relheight=0.11)


    #menu labels
    itemslabel = tk.Label(mainframe, text="Items", font=("Sitka Display", 13, 'bold', 'underline'), bg='white')
    itemslabel.place(relx=0.015, rely=0.01, relwidth=0.12, relheight=0.08)
    pricelabel = tk.Label(mainframe, text="Price", font=("Sitka Display", 13, 'bold', 'underline'), bg='white')
    pricelabel.place(relx=0.535, rely=0.01, relheight=0.08, relwidth=0.12)

    # To insert column with menu items
    get_kfc_list = getitems_kfc_menu(meal_name)
    i = 4
    counter1 = 0
    for a in get_kfc_list:
        Label1 = tk.Label(menuframe1, text=get_kfc_list[counter1], anchor = 'center')
        Label1.grid(row=i, column=1, sticky='w')
        # Label1.place(relx=0.05, rely=0.05+i*0.01, relwidth=0.35)
        Label1.config(font=("Corbel Light", 12), bg='white')
        i += 1
        counter1 += 1

    # To insert a column to display the corresponding prices:
    get_kfc_price_list = getitems_kfc_price(meal_name)
    j = 4
    counter2 = 0
    for b in get_kfc_price_list:
        Label2 = tk.Label(menuframe2, text=get_kfc_price_list[counter2], anchor = 'center')
        Label2.grid(row=j, column=1, sticky='w')
        Label2.config(font=("Corbel Light", 12), bg='white')
        j += 1
        counter2 += 1


    window.resizable(False,False)
    window.mainloop()



    


