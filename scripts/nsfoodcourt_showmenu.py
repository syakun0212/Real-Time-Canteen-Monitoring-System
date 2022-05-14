import tkinter as tk
from PIL import Image, ImageTk
from nsfoodcourt_menulists_function import getitems, getprice
from operatinghours import show_operation_hours
from calculatetime import calculatetimewindow

#function that creates a new window to display the menu for NorthSpine (NS) food court stores
def new_window(store_name,operating_hours_name):#(Yakun & Shannon)

    ##Dictionary to store the information for background image of NorthSpine (NS) food court menus
    imagedict = {"MiniWok": "miniwok.png",
                 "ChickenRice": "chickenrice.png",
                 "Viet": "viet.png",
                 "Noodles": "noodles.png",
                 "Western": "western.png",
                 "Malay": "malay.png",
                 "Indian": "indian.png",
                 "Salad": "salad.png",
                 "Chinese": "chinese.png",
                 "Claypot": "claypot.png",
                 "ClaypotMon": "claypot.png",
                 "ClaypotTues": "claypot.png",
                 "ClaypotWed": "claypot.png",
                 "ClaypotThurs": "claypot.png",
                 "ClaypotFri": "claypot.png",
                 "ClaypotSat": "claypot.png"}

    #DIctionary to store the title(name) of stores that is to be displayed on top of the menu
    storenamedict = {"MiniWok": "MINI WOK",
                     "ChickenRice": "CHICKEN RICE",
                     "Viet": "VIETNAMESE FOOD",
                     "Noodles": "HANDMADE NOODLES",
                     "Western": "WESTERN FOOD",
                     "Malay": "MALAY CUISINE",
                     "Indian": "INDIAN CUISINE",
                     "Salad": "HEALTHY SALAD",
                     "Chinese": "CHINESE FOOD",
                     "Claypot": "CLAYPOT DELIGHTS",
                     "ClaypotMon": "CLAYPOT DELIGHTS",
                     "ClaypotTues": "CLAYPOT DELIGHTS",
                     "ClaypotWed": "CLAYPOT DELIGHTS",
                     "ClaypotThurs": "CLAYPOT DELIGHTS",
                     "ClaypotFri": "CLAYPOT DELIGHTS",
                     "ClaypotSat": "CLAYPOT DELIGHTS"}

    window = tk.Tk()  # create window
    window.geometry("500x500+350+70")  # size of window: window width x window height + position right + position down
    window.configure(background='white')  # colour of window background
    window.title('Northspine Food Court')  # name of window

    #create frame and label to display background pictures and name of the stores
    mainframe = tk.Frame(window, bg='white')
    mainframe.place(relwidth=1, relheight=1)
    background_image = Image.open(imagedict[store_name])
    background_image = ImageTk.PhotoImage(background_image,master=window)
    background_label = tk.Label(mainframe, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Insert menu information
    # function to display menu for Claypot store (the store that has special menu everyday)
    if store_name in ["ClaypotMon", "ClaypotTues", "ClaypotWed", "ClaypotThurs", "ClaypotFri", "ClaypotSat"]:

        menuframe1 = tk.Frame(window, bg='White')
        menuframe1.place(relx=0.07, rely=0.57, relheight=0.5, relwidth=0.52)
        menuframe2 = tk.Frame(window, bg='white')
        menuframe2.place(relx=0.60, rely=0.57, relheight=0.5, relwidth=0.12)
        menuframe3 = tk.Frame(window, bg='Orange')
        menuframe3.place(relx=0.07, rely=0.47, relheight=0.1, relwidth=0.52)
        menuframe4 = tk.Frame(window, bg='Orange')
        menuframe4.place(relx=0.60, rely=0.47, relheight=0.1, relwidth=0.12)

        #insert column for special dishes at the top of the menu (words to be highlighed)
        i = 4
        counter1 = 0
        getitemsList1 = getitems("Claypot")
        for a in getitemsList1:
            Label1 = tk.Label(menuframe1, text=getitemsList1[counter1])
            Label1.grid(row=i, column=1, sticky='w')
            Label1.config(font=("Calibri", 13), bg='white')
            i += 1
            counter1 += 1

        #insert normal daily menu below the special dishes
        getitemsList2 = getitems(store_name)
        i = 4
        counter1 = 0

        for b in getitemsList2:
            Label1day = tk.Label(menuframe3, text=getitemsList2[counter1])
            Label1day.grid(row=i, column=1, sticky='w')
            Label1day.config(font=("Calibri", 13), bg='orange')
            i += 1
            counter1 += 1

        #insert corresponding prices for special dishes
        j = 4
        counter2 = 0
        getpriceList1 = getprice("Claypot")
        for c in getpriceList1:
            Label1 = tk.Label(menuframe2, text=getpriceList1[counter2])
            Label1.grid(row=j, column=1, sticky='w')
            Label1.config(font=("Calibri", 13), bg='white')
            j += 1
            counter2 += 1

        #insert corresponding prices for normal daily dishes
        j = 4
        counter2 = 0
        getpriceList2 = getprice(store_name)
        for d in getpriceList2:
            Label2day = tk.Label(menuframe4, text=getpriceList2[counter2])
            Label2day.grid(row=j, column=1, sticky='w')
            Label2day.config(font=("Calibri", 13), bg='orange')
            j += 1
            counter2 += 1

    #function to display menu information for other stores in NS food court (which do not have special menus)
    else:
        getitemsList = getitems(store_name)
        getpriceList = getprice(store_name)

        #create frames to display menu and price information
        menuframe5 = tk.Frame(window, bg='white')
        menuframe5.place(relx=0.07, rely=0.47, relheight=0.5, relwidth=0.52)
        menuframe6 = tk.Frame(window, bg='white')
        menuframe6.place(relx=0.60, rely=0.47, relheight=0.5, relwidth=0.12)

        #insert columns of menu items
        i = 4
        counter1 = 0
        for a in getitemsList:
            Label1 = tk.Label(menuframe5, text=getitemsList[counter1])
            Label1.grid(row=i, column=1, sticky='w')
            Label1.config(font=("Calibri", 13), bg='white')
            i += 1
            counter1 += 1

        #insert columns of corresponding prices
        j = 4
        counter2 = 0
        for b in getpriceList:
            Label2 = tk.Label(menuframe6, text=getpriceList[counter2])
            Label2.grid(row=j, column=2, sticky='w')
            Label2.config(font=("Calibri", 13), bg='white')
            j += 1
            counter2 += 1

    #create labels for menu
    itemslabel = tk.Label(mainframe, text="Items", font=("Calibri", 13, 'bold', 'underline'), bg='white',fg='black')
    itemslabel.place(relx=0.07, rely=0.42)
    pricelabel = tk.Label(mainframe, text="Price", font=("Calibri", 13, 'bold', 'underline'), bg='white',fg='black')
    pricelabel.place(relx=0.60, rely=0.42)
    storelabel = tk.Label(mainframe,text=storenamedict[store_name],font=("MS Gothic", 30, 'bold'), bg='white',fg='black')
    storelabel.place(relx=0.15,rely=0.15,relwidth=0.70,relheight=0.10)

    #command for operating hours for different stores (when click the 'operating hours' button)
    if operating_hours_name == 'McDonalds':
       operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange', fg='white', 
                                        font=("Calibri", 11, 'bold'), relief="ridge", borderwidth=1,
                                        command=lambda: show_operation_hours("McDonalds", mainframe))
       operatinghoursbutton.place(relx=0.73, rely=0.45, relheight=0.06, relwidth=0.24)
    elif operating_hours_name == 'starbucks':
       operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange', fg='white', 
                                        font=("Calibri", 11, 'bold'), relief="ridge", borderwidth=1,
                                        command=lambda: show_operation_hours("McDonalds", mainframe))
       operatinghoursbutton.place(relx=0.73, rely=0.45, relheight=0.06, relwidth=0.24)
    elif operating_hours_name == 'KFC':
       operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange', fg='white', 
                                        font=("Calibri", 11, 'bold'), relief="ridge", borderwidth=1,
                                        command=lambda: show_operation_hours("McDonalds", mainframe))
       operatinghoursbutton.place(relx=0.73, rely=0.45, relheight=0.06, relwidth=0.24)
    elif operating_hours_name == 'Northspine Food Court':
       operatinghoursbutton = tk.Button(mainframe, text='Operating Hours', bg='orange', fg='white', 
                                        font=("Calibri", 11, 'bold'), relief="ridge", borderwidth=1,
                                        command=lambda: show_operation_hours("Northspine Food Court", mainframe))
       operatinghoursbutton.place(relx=0.73, rely=0.45, relheight=0.06, relwidth=0.24)

    #waiting time and quit button
    waitingtimebutton = tk.Button(mainframe, text='Waiting Time', bg='orange', fg='white', font=("Calibri", 11, 'bold'),relief="ridge", borderwidth=1,command=lambda:calculatetimewindow())
    waitingtimebutton.place(relx=0.73, rely=0.53, relheight=0.06, relwidth=0.24)
    backBtn = tk.Button(mainframe, text="<  Quit", bg='orange', fg='white', command=window.destroy,font=("Calibri", 11, 'bold'),relief="ridge", borderwidth=1)
    backBtn.place(relx=0.78, rely=0.9, relwidth=0.18, relheight=0.06)

    #lock the window size
    window.resizable(False, False)

    window.mainloop()