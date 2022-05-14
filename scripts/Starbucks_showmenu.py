import csv
import tkinter as tk
from PIL import Image, ImageTk
from calculatetime import calculatetimewindow
from operatinghours import show_operation_hours
import PIL

#function to make starbucks menu information from the csv file into lists
def starbucksmenu(): #(Yakun & Shannon)
    with open('starbucks_menu.csv', mode='r') as csv_file:
        starbucksitems = csv.DictReader(csv_file)
        itemslist = []
        drinksMlist = []
        drinksLlist = []
        drinksXLlist = []
        for row in starbucksitems:
            itemslist.append(row["Starbucks_drinks_menu"])
            drinksMlist.append(row["Starbucks_Drinks_price_M"])
            drinksLlist.append(row["Starbucks_Drinks_price_L"])
            drinksXLlist.append(row["Starbucks_Drinks_price_XL"])
        return itemslist, drinksMlist, drinksLlist, drinksXLlist

#function to display the starbucks menu window
def displaystarbucksmenu(): #(Yakun & Shannon)
    window = tk.Tk()#create a new window
    window.geometry("500x500+350+70")# size of window: window width x window height + position right + position down
    window.configure(background='white')#background colour of the window
    window.title('Starbucks')#title of the window

    #put in background image
    background_image = Image.open('starbucks_background.jpg')
    background_image = ImageTk.PhotoImage(background_image, master=window)
    background_label = tk.Label(window)
    background_label.config(image = background_image)
    background_label.pack()

    #create frames to display the menu information
    mainframe = tk.Frame(window, bg='#314337')
    mainframe.place(relx=0.07, rely=0.35,relwidth=0.9, relheight=0.6)

    menuframe = tk.Frame(window, bg='#314337')
    menuframe.place(relx=0.07, rely=0.42, relheight=0.55, relwidth=0.63)

    #insert columns  to display menu items
    i = 0
    j = 0
    counter1 = 0
    while counter1 < len(starbucksmenu()):                #iterate through the tuple from starbucksmenu() function
        counter2 = 0
        while counter2 < len(starbucksmenu()[counter1]):   #iterate through the list
            Label1 = tk.Label(menuframe, text=starbucksmenu()[counter1][counter2])
            Label1.grid(row=i, column=j, sticky='w')
            Label1.config(font=("Corbel Light", 13),bg='#314337', fg='white')
            counter2 += 1
            i +=1
            if i > 8:
                j +=1                           #next list will display on another column
                i = 0
                break


        counter1 += 1

    #insert menu labels
    itemslabel = tk.Label(mainframe, text="Items", font=("Sitka Display", 13, 'bold', 'underline'), bg='#314337', fg='white')
    itemslabel.place(relx=0.03, rely=0)
    pricelabel1 = tk.Label(mainframe, text="Tall", font=("Sitka Display", 13, 'bold', 'underline'), bg='#314337', fg='white')
    pricelabel1.place(relx=0.38, rely=0)
    pricelabel2 = tk.Label(mainframe, text="Grande", font=("Sitka Display", 13, 'bold', 'underline'), bg='#314337', fg='white')
    pricelabel2.place(relx=0.47, rely=0)
    pricelabel3 = tk.Label(mainframe, text="Venti", font=("Sitka Display", 13, 'bold', 'underline'), bg='#314337', fg='white')
    pricelabel3.place(relx=0.60, rely=0)


    #buttons for operating hours, waiting time, and quit
    operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='#DEAD3F', fg='black', font=("Sitka Display", 11),relief = 'ridge', borderwidth = 1,command=lambda: show_operation_hours("starbucks", mainframe))
    operatinghoursbutton.place(relx=0.74, rely=0.15, relheight=0.1, relwidth=0.25)
    waitingtimebutton = tk.Button(mainframe, text='Waiting Time',  bg='#DEAD3F', fg='black', font=("Sitka Display", 11),relief = 'ridge', borderwidth = 1,command=lambda:calculatetimewindow())
    waitingtimebutton.place(relx=0.74, rely=0.29, relheight=0.1, relwidth=0.25)

    backBtn = tk.Button(mainframe, text="< Quit", bg='#B07522', fg='black',relief = 'ridge',  font=("Sitka Display", 11),borderwidth = 1, command=window.destroy)
    backBtn.place(relx=0.86, rely=0.88, relwidth=0.11, relheight=0.09)

    window.resizable(False,False)
    window.mainloop()