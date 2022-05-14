import tkinter as tk
from PIL import Image, ImageTk  
from datetime import datetime, date
import time
from tkcalendar import Calendar
from tkinter import messagebox
from nsfoodcourt_showmenu import new_window
from mcdonalds_showmenu import getitems_Mcdonalds, show_McDonalds_menu
from kfc_showmenu import show_kfc_menu,getitems_kfc_price,getitems_kfc_menu 
from operatinghours import show_operation_hours
from Starbucks_showmenu import starbucksmenu, displaystarbucksmenu
import json

def calendar(): #creates a calendar to allow user to manually pick date and input time (Jackson)
    def get_newdt(): #get user-defined time from entry and apply exceptional handling
        while True:
            newtime = timeentry.get()
            try:
                newtime = int(timeentry.get())
            except:
                messagebox.showinfo("Error", "Please enter in the correct format")
                top.destroy()
                calendar()
            if not (0 <= newtime <= 59 or 100 <= newtime <= 159 or 200 <= newtime <= 259 or 300 <= newtime <= 359 \
                    or 400 <= newtime <= 459 or 500 <= newtime <= 559 or 600 <= newtime <= 659 or 700 <= newtime <= 759 \
                    or 800 <= newtime <= 859 or 900 <= newtime <= 959 or 1000 <= newtime <= 1059 or 1100 <= newtime <= 1159 \
                    or 1200 <= newtime <= 1259 or 1300 <= newtime <= 1359 or 1400 <= newtime <= 1459 or 1500 <= newtime <= 1559 \
                    or 1600 <= newtime <= 1659 or 1700 <= newtime <= 1759 or 1800 <= newtime <= 1859 or 1900 <= newtime <= 1959 \
                    or 2000 <= newtime <= 2059 or 2100 <= newtime <= 2159 or 2200 <= newtime <= 2259 or 2300 <= newtime <= 2359):

                messagebox.showinfo("Error", "Please enter in the correct format")
                top.destroy()
                calendar()
            else:
                break
        top.destroy()
        newdate = cal.selection_get()
        newday = newdate.strftime('%A')
        getstores(int(newtime), newday)

    day_int = int(now.strftime("%d"))
    month_int = int(now.strftime("%m"))
    year_int = int(now.strftime("%Y"))
    top = tk.Tk()
    top.geometry("+450+150")
    top.title("Date and Time Picker")
    canvas2 = tk.Canvas(top, height=50, width=50)
    canvas2.pack(side='bottom')

    cal = Calendar(top,
                   font="Arial 12", selectmode='day',
                   cursor="hand2", year=year_int, month=month_int, day=day_int)
    cal.pack(fill='x', expand=False)

    label1 = tk.Label(top, text="Enter the time in 24h format here:")
    label1.place(rely=0.82)
    timeentry = tk.Entry(top)
    timeentry.place(relx=0.6, rely=0.82, relwidth=0.2)
    label2 = tk.Label(top, text="eg.1430")
    label2.place(relx=0.82, rely=0.82)
    btn1 = tk.Button(top, text="Ok", command=get_newdt)
    btn1.place(relx=0.5, rely=0.9)

    top.resizable(False, False)
    top.mainloop()

#Main Program Starts Here (Jackson)
root = tk.Tk()
root.geometry("500x500+350+70")
root.title('Northspine Food Information System')

mainframe = tk.Frame(root)
mainframe.place(relwidth=1,relheight=1)

background_image = ImageTk.PhotoImage(file='welcome.png')
background_label = tk.Label(mainframe, image=background_image)
background_label.place(relwidth=1,relheight=1)

dtframe = tk.Frame(mainframe,bg="white",bd=5)
dtframe.place(relx=0.35,rely=0.05,relwidth=0.35,relheight=0.23)

day= datetime.today().strftime('%A')
label2 = tk.Label(dtframe,text=day,font=("helvetica",19,"bold"),bg="white", fg="orange")
label2.pack()

today= date.today().strftime('%d %b %Y')
label1 = tk.Label(dtframe,text=today,font=("helvetica",19,"bold"),bg="white", fg="orange")
label1.pack()

time1 = ''
clock = tk.Label(dtframe, font=("helvetica",19,"bold"), bg='white', fg='orange')
clock.pack()

def tick(): #updates the clock every 200ms (Jackson)
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()

now = datetime.now()
dt_string = now.strftime("%d/%m/%y\n%H:%M:%S")
time_now = int(now.strftime("%H%M"))
day_now = now.strftime("%A")

btn1 = tk.Button(mainframe, text="View Current Stores", bg='orange', fg='white',
                 relief='ridge',borderwidth=1,font=("helvetica",10,"bold"),command=lambda: getstores(time_now, day))
btn1.place(relx=0.325,rely=0.51, relwidth=0.4,relheight=0.07)

btn2 = tk.Button(mainframe, text="View Stores by Other Dates", bg='orange', fg='white',
                 relief='ridge',borderwidth=1,font=("helvetica",10,"bold"), command=calendar)
btn2.place(relx=0.325,rely=0.59, relwidth=0.4,relheight=0.07)

exitBtn = tk.Button(mainframe,text="<  Quit",bg='orange', fg='white',command=quit,relief='ridge',borderwidth=1,
                    font=("helvetica",10,"bold"))
exitBtn.place(relx=0.44,rely=0.67, relwidth=0.18,relheight=0.07)

def getstores(time, day): #creates a new frame to dislay list of stores available (Jackson)
    
    firstframe = tk.Frame(mainframe)
    firstframe.place(relwidth=1, relheight=1)


    background_image = ImageTk.PhotoImage(file='page2.png')
    background_label = tk.Label(firstframe, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    mcdonald = Image.open("mcdonald2.jpeg")
    mcdonald = mcdonald.resize((120,120))
    mcdonald = ImageTk.PhotoImage(mcdonald)
    macsclosed = Image.open("macsclosed.png")
    macsclosed = macsclosed.resize((120,120))
    macsclosed = ImageTk.PhotoImage(macsclosed)

    kfc = Image.open("KFC.jpeg")
    kfc = kfc.resize((120, 120))
    kfc = ImageTk.PhotoImage(kfc)
    kfcclosed = Image.open("kfcclosed.png")
    kfcclosed = kfcclosed.resize((120, 120))
    kfcclosed = ImageTk.PhotoImage(kfcclosed)

    starbucks = Image.open("starbucks.gif")
    starbucks = starbucks.resize((120, 120))
    starbucks = ImageTk.PhotoImage(starbucks)
    sbclosed = Image.open("sbclosed.png")
    sbclosed = sbclosed.resize((120, 120))
    sbclosed = ImageTk.PhotoImage(sbclosed)

    def mcdonalds_frame(): #creates a new frame for McDonalds to show different options (EVMs, Drinks, Sides etc.) (Yakun)

        mcdonalds_frame = tk.Frame(firstframe, bg="orange")
        mcdonalds_frame.place(relwidth=1, relheight=1)

        background_image = ImageTk.PhotoImage(file='Mcdonalds_main background.jpg')
        background_label = tk.Label(mcdonalds_frame, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        mcbtn1 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Value Meal', font=("Ink Free", 20,'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('ValueMeal', 'ValueMeal_price'))
        mcbtn1.place(relx=0.14, rely=0.36, relheight=0.11, relwidth=0.5)

        mcbtn2 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Sides', font=("Ink Free", 20,'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Sides', 'Sides_Price'))
        mcbtn2.place(relx=0.14, rely=0.50, relheight=0.11, relwidth=0.5)

        mcbtn3 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Dessert', font=("Ink Free", 20,'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Dessert', 'Dessert_price'))
        mcbtn3.place(relx=0.14, rely=0.64, relheight=0.11, relwidth=0.5)

        mcbtn4 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Beverages', font=("Ink Free", 20,'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Beverages', 'Beverages_price'))
        mcbtn4.place(relx=0.14, rely=0.78, relheight=0.11, relwidth=0.5)

        mcback = tk.Button(mcdonalds_frame, text="< Back", bg='#E89359', fg='white', font=("Ink Free", 14,'bold'),
                           relief='ridge', borderwidth=1, command=mcdonalds_frame.place_forget)
        mcback.place(relx=0.83, rely=0.90, relwidth=0.13, relheight=0.05)
        mcdonalds_frame.mainloop()

    def mcdonalds_full_frame(): #same as mcdonalds_frame with the inclusion of Breakfast menu (Yakun)


        mcdonalds_frame = tk.Frame(firstframe, bg="black")
        mcdonalds_frame.place(relwidth=1, relheight=1)

        background_image = ImageTk.PhotoImage(
            file='Mcdonalds_main background.jpg')
        background_label = tk.Label(mcdonalds_frame, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        mcbtn1 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Breakfast',
                           font=("Ink Free", 18, 'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Breakfast', 'Breakfast_price'))
        mcbtn1.place(relx=0.14, rely=0.32, relheight=0.09, relwidth=0.5)


        mcbtn2 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Value Meal',
                           font=("Ink Free", 18, 'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('ValueMeal', 'ValueMeal_price'))
        mcbtn2.place(relx=0.14, rely=0.43, relheight=0.09, relwidth=0.5)

        mcbtn3 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Sides', font=("Ink Free", 18, 'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Sides', 'Sides_Price'))
        mcbtn3.place(relx=0.14, rely=0.54, relheight=0.09, relwidth=0.5)

        mcbtn4 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Dessert', font=("Ink Free", 18, 'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Dessert', 'Dessert_price'))
        mcbtn4.place(relx=0.14, rely=0.65, relheight=0.09, relwidth=0.5)

        mcbtn5 = tk.Button(mcdonalds_frame, bg='#F1795F', fg='white', text='Beverages',
                           font=("Ink Free", 18, 'bold'),
                           relief='ridge', borderwidth=1,
                           command=lambda: show_McDonalds_menu('Beverages', 'Beverages_price'))
        mcbtn5.place(relx=0.14, rely=0.76, relheight=0.09, relwidth=0.5)

        mcback = tk.Button(mcdonalds_frame, text="< Back", bg='#E89359', fg='white', font=("Ink Free", 14, 'bold'),
                           relief='ridge', borderwidth=1, command=mcdonalds_frame.place_forget)
        mcback.place(relx=0.83, rely=0.90, relwidth=0.13, relheight=0.05)

        mcdonalds_frame.mainloop()

    #McDonalds (Custom buttons with different commands based on day and time) (Jackson)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if day in weekdays:
        if 700 <= time <= 1059:
            button1 = tk.Button(firstframe, image=mcdonald, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command=lambda: show_McDonalds_menu('Breakfast', 'Breakfast_price'))
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)
        elif 1100 <= time <= 2359:
            button1 = tk.Button(firstframe, image=mcdonald, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command=mcdonalds_frame)
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)
        else:
            button1 = tk.Button(firstframe, image=macsclosed, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command = lambda:  show_ask_window('McDonalds',firstframe))
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)
    else:
        if 1000 <= time <= 1059:
            button1 = tk.Button(firstframe, image=mcdonald, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command=lambda: show_McDonalds_menu('Breakfast', 'Breakfast_price'))
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)
        elif 1100 <= time <= 2209:
            button1 = tk.Button(firstframe, image=mcdonald, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command=mcdonalds_frame)
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)    
        else:
            button1 = tk.Button(firstframe, image=macsclosed, bg='black', fg='white',relief='ridge',borderwidth=1,
                                command = lambda:  show_ask_window('McDonalds',firstframe))
            button1.place(relx=0.075, rely=0.07, relheight=0.25, relwidth=0.25)

    def kfc_frame(): #creates a new frame for KFC to show different options (Deals, Drinks, Sides etc.) (Yakun)
       
        kfc_frame = tk.Frame(firstframe, bg="orange")
        kfc_frame.place(relwidth=1, relheight=1)

        background_image = ImageTk.PhotoImage(file='kfc_main_background.jpg')
        background_label = tk.Label(kfc_frame, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        kfcbtn1 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Hot Deals', font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('HotDeals'))
        kfcbtn1.place(relx=0.1, rely=0.25, relheight=0.08, relwidth=0.33)

        kfcbtn2 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Boxes', font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('Boxes'))
        kfcbtn2.place(relx=0.48, rely=0.25, relheight=0.08, relwidth=0.31)

        kfcbtn3 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Chicken A La Carte',font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('Chicken'))
        kfcbtn3.place(relx=0.1, rely=0.35, relheight=0.08, relwidth=0.33)

        kfcbtn4 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Chicken Meal',font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('ChickenMeals'))
        kfcbtn4.place(relx=0.48, rely=0.35, relheight=0.08, relwidth=0.31)

        kfcbtn5 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Bowl A La Carte', font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('Bowls'))
        kfcbtn5.place(relx=0.1, rely=0.45, relheight=0.08, relwidth=0.33)

        kfcbtn6 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Bowl Meals', font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('BowlMeals'))
        kfcbtn6.place(relx=0.48, rely=0.45, relheight=0.08, relwidth=0.31)

        kfcbtn7 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Burger A La Carte', font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('Burger'))
        kfcbtn7.place(relx=0.1, rely=0.55, relheight=0.08, relwidth=0.33)

        kfcbtn8 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Burger Meals',font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1,  command=lambda: show_kfc_menu('BurgerMeals'))
        kfcbtn8.place(relx=0.48, rely=0.55, relheight=0.08, relwidth=0.31)

        kfcbtn9 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Sharing 5',font=("Ink Free", 13,'bold'),
                            relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('sharing5'))
        kfcbtn9.place(relx=0.1, rely=0.65, relheight=0.08, relwidth=0.33)

        kfcbtn10 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Sharing 24', font=("Ink Free", 13,'bold'),
                             relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('sharing24'))
        kfcbtn10.place(relx=0.48, rely=0.65, relheight=0.08, relwidth=0.31)

        kfcbtn11 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Sides',font=("Ink Free", 13,'bold'),
                             relief = 'ridge', borderwidth = 1,  command=lambda: show_kfc_menu('sides'))
        kfcbtn11.place(relx=0.1, rely=0.75, relheight=0.08, relwidth=0.33)

        kfcbtn12 = tk.Button(kfc_frame, bg='#DC493A', fg='white', text='Drinks', font=("Ink Free", 13,'bold'),
                             relief = 'ridge', borderwidth = 1, command=lambda: show_kfc_menu('drinks'))
        kfcbtn12.place(relx=0.48, rely=0.75, relheight=0.08, relwidth=0.31)

        kfcback = tk.Button(kfc_frame, text="<  Back", bg='#C3701F', fg='white', font=("Ink Free", 10,'bold'),
                            relief = 'ridge', borderwidth = 1, command = kfc_frame.place_forget)
        kfcback.place(relx=0.64, rely=0.85, relheight=0.05, relwidth=0.15)

        kfc_frame.mainloop()

    #KFC (Custom buttons with different commands based on day and time) (Jackson)
    if day in weekdays:
        if 730 <= time <= 2200:
            button2 = tk.Button(firstframe, image=kfc, bg='black',relief='ridge',borderwidth=1,command=kfc_frame)
            button2.place(relx=0.375, rely=0.07, relheight=0.25, relwidth=0.25)
        else:
            button2 = tk.Button(firstframe, image=kfcclosed, bg='black',relief='ridge',borderwidth=1,
                command = lambda: show_ask_window('KFC',firstframe))
            button2.place(relx=0.375, rely=0.07, relheight=0.25, relwidth=0.25)
    else:
        if 1100 <= time <= 2000:
            button2 = tk.Button(firstframe, image=kfc, bg='black',relief='ridge',borderwidth=1,command=kfc_frame)
            button2.place(relx=0.375, rely=0.07, relheight=0.25, relwidth=0.25)
        else:
            button2 = tk.Button(firstframe, image=kfcclosed, bg='black',relief='ridge',borderwidth=1,
                command = lambda: show_ask_window('KFC',firstframe))
            button2.place(relx=0.375, rely=0.07, relheight=0.25, relwidth=0.25)
    #Starbucks (Custom buttons with different commands based on day and time) (Jackson)
    if day in weekdays:
        if 700 <= time <= 2200:
            button3 = tk.Button(firstframe, image=starbucks, bg='black', fg='white', command = displaystarbucksmenu)
            button3.place(relx=0.675, rely=0.07, relheight=0.25, relwidth=0.25)

        else:
            button3 = tk.Button(firstframe, image=sbclosed, bg='black', fg='white',
                command = lambda:show_ask_window('starbucks',firstframe))
            button3.place(relx=0.675, rely=0.07, relheight=0.25, relwidth=0.25)
    else:
        if 700 <= time <= 1700:
            button3 = tk.Button(firstframe, image=starbucks, bg='black', fg='white',command = displaystarbucksmenu)
            button3.place(relx=0.675, rely=0.07, relheight=0.25, relwidth=0.25)

        else:
            button3 = tk.Button(firstframe, image=sbclosed, bg='black', fg='white',
                command = lambda:show_ask_window('starbucks',firstframe))
            button3.place(relx=0.675, rely=0.07, relheight=0.25, relwidth=0.25)
    
    def nsCanteen(): #creates new frame to list down all NS Canteen stores (Jackson)

        nsFrame = tk.Frame(firstframe, bg="orange")
        nsFrame.place(relwidth=1, relheight=1)

        background_image = ImageTk.PhotoImage(file='page2.png')
        background_label = tk.Label(nsFrame, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        nsbtn1 = tk.Button(nsFrame, bg='orange', fg='white', text='Mini Wok',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('MiniWok','Northspine Food Court'))
        nsbtn1.place(relx=0.1, rely=0.1, relheight=0.10, relwidth=0.35)

        nsbtn2 = tk.Button(nsFrame, bg='orange', fg='white', text='Chicken Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ChickenRice','Northspine Food Court'))
        nsbtn2.place(relx=0.1, rely=0.22, relheight=0.1, relwidth=0.35)

        nsbtn3 = tk.Button(nsFrame, bg='orange', fg='white', text='Vietnamese Food',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Viet','Northspine Food Court'))
        nsbtn3.place(relx=0.1, rely=0.34, relheight=0.1, relwidth=0.35)

        nsbtn4 = tk.Button(nsFrame, bg='orange', fg='white', text='Handmade Noodles',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Noodles','Northspine Food Court'))
        nsbtn4.place(relx=0.1, rely=0.46, relheight=0.1, relwidth=0.35)

        nsbtn5 = tk.Button(nsFrame, bg='orange', fg='white', text='Western Food',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Western','Northspine Food Court'))
        nsbtn5.place(relx=0.1, rely=0.58, relheight=0.1, relwidth=0.35)

        nsbtn6 = tk.Button(nsFrame, bg='orange', fg='white', text='Malay Food',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Malay','Northspine Food Court'))
        nsbtn6.place(relx=0.55, rely=0.1, relheight=0.1, relwidth=0.35)

        nsbtn7 = tk.Button(nsFrame, bg='orange', fg='white', text='Indian Food',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Indian','Northspine Food Court'))
        nsbtn7.place(relx=0.55, rely=0.22, relheight=0.1, relwidth=0.35)

        nsbtn8 = tk.Button(nsFrame, bg='orange', fg='white', text='Salad',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Salad','Northspine Food Court'))
        nsbtn8.place(relx=0.55, rely=0.34, relheight=0.1, relwidth=0.35)

        nsbtn9 = tk.Button(nsFrame, bg='orange', fg='white', text='Chinese Delights',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Chinese','Northspine Food Court'))
        nsbtn9.place(relx=0.55, rely=0.46, relheight=0.1, relwidth=0.35)

        #function to call for special menu on different days for 'Claypot' store (Jackson)
        if day == 'Monday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotMon','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Tuesday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotTues','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Wednesday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotWed','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Thursday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotThurs','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Friday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotFri','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Saturday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('ClaypotSat','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        if day == 'Sunday':

            nsbtn10 = tk.Button(nsFrame, bg='orange', fg='white', text='Claypot Rice',font=("Calibri", 15, "bold"),
                            relief='ridge',borderwidth=1,command=lambda:new_window('Claypot','Northspine Food Court'))
            nsbtn10.place(relx=0.55, rely=0.58, relheight=0.1, relwidth=0.35)

        nsback = tk.Button(nsFrame, text="<  Back", bg='orange', fg='white',
                        command=nsFrame.place_forget,font=("Calibri", 15, "bold"),relief='ridge',borderwidth=1)
        nsback.place(relx=0.8, rely=0.9, relwidth=0.18, relheight=0.06)

        nsFrame.mainloop()
    #Northspine Canteen (Custom buttons with different commands based on day and time) (Jackson)
    if day in weekdays:
        if 730 <= time <= 2030:

            button4 = tk.Button(firstframe, bg='orange', fg='white', text="North Spine Canteen",
                            font=("MS Gothic", 28, "bold"), command=nsCanteen,relief='ridge',borderwidth=1)
            button4.place(relx=0.075, rely=0.4, relheight=0.25, relwidth=0.85)

        else:
            button4 = tk.Button(firstframe, bg='orange', fg='white', text="Closed", font=("MS Gothic", 72, "bold"),
                                command = lambda: show_ask_window('Northspine Food Court',firstframe))
            button4.place(relx=0.075, rely=0.4, relheight=0.25, relwidth=0.85)

    elif day == 'Saturday':
        if 900 <= time <= 2000:

            button4 = tk.Button(firstframe, bg='orange', fg='white', text="North Spine Canteen",
                            font=("MS Gothic", 28, "bold"), command=nsCanteen,relief='ridge',borderwidth=1)
            button4.place(relx=0.075, rely=0.4, relheight=0.25, relwidth=0.85)

        else:
            button4 = tk.Button(firstframe, bg='orange', fg='white', text="Closed", font=("MS Gothic", 72, "bold"),
                                command = lambda: show_ask_window('Northspine Food Court',firstframe))
            button4.place(relx=0.075, rely=0.4, relheight=0.25, relwidth=0.85)
    else:
        button4 = tk.Button(firstframe, bg='orange', fg='white', text="Closed", font=("MS Gothic", 72, "bold"),
                            command = lambda: show_ask_window('Northspine Food Court',firstframe))
        button4.place(relx=0.075, rely=0.4, relheight=0.25, relwidth=0.85)

    backBtn = tk.Button(firstframe, text="<  Back", bg='orange', fg='white', command=firstframe.place_forget,
                        font=("Calibri", 15, "bold"),relief='ridge',borderwidth=1)
    backBtn.place(relx=0.8, rely=0.9, relwidth=0.18, relheight=0.06)


    def show_ask_window(store_name, window): #creates a pop-up menu when store is closed to display operating hours
                                             #prompts user whether they still want to view menu (Yakun)

        with open('operating_hours_jsonfile.json','r') as f:
            operating_hours = json.load(f)

            ask_windows = tk.Toplevel(window, bg='#F0C35D')
            ask_windows.title("Operating Hours of " + store_name)
            ask_windows.geometry("350x350+350+70")

            main_label = tk.Label(ask_windows, text='Operating Hours', bg='#F0C35D',
                                  font=("Berlin Sans FB Demi", 24, 'bold'), fg='black')
            main_label.place(relx=0.15, rely=0.1)

            content_label = tk.Label(ask_windows, text=operating_hours[store_name], bg='#F0C35D', font=("Ink Free", 16))
            content_label.place(relx=0.1, rely=0.3, relwidth=0.8)

            ask_label = tk.Label(ask_windows, text='The store is closed, \ndo you still want to check the menu?',
                                 font=("Berlin Sans FB Demi", 14, 'bold'), fg='black')
            ask_label.place(relx=0.02, rely=0.56, relwidth=0.95)

            no_button = tk.Button(ask_windows, bg='#DC493A', fg='white', text='no', font=("Ink Free", 13, 'bold'),
                                  relief='ridge', borderwidth=1, command=lambda: ask_windows.destroy())
            no_button.place(relx=0.6, rely=0.81, relheight=0.08, relwidth=0.28)

            if store_name == 'KFC':
                yes_button = tk.Button(ask_windows, bg='#DC493A', fg='white', text='Yes', font=("Ink Free", 13, 'bold'),
                                       relief='ridge', borderwidth=1,
                                       command=lambda: [f() for f in [ask_windows.destroy(), kfc_frame()]])
                yes_button.place(relx=0.1, rely=0.81, relheight=0.08, relwidth=0.28)

            elif store_name == 'starbucks':
                yes_button = tk.Button(ask_windows, bg='#DC493A', fg='white', text='Yes', font=("Ink Free", 13, 'bold'),
                                       relief='ridge', borderwidth=1,
                                       command=lambda: [f() for f in [ask_windows.destroy(), displaystarbucksmenu()]])
                yes_button.place(relx=0.1, rely=0.81, relheight=0.08, relwidth=0.28)

            elif store_name == 'Northspine Food Court':
                yes_button = tk.Button(ask_windows, bg='#DC493A', fg='white', text='Yes', font=("Ink Free", 13, 'bold'),
                                       relief='ridge', borderwidth=1,
                                       command=lambda: [f() for f in [ask_windows.destroy(), nsCanteen()]])
                yes_button.place(relx=0.1, rely=0.81, relheight=0.08, relwidth=0.28)

            elif store_name == 'McDonalds':
                yes_button = tk.Button(ask_windows, bg='#DC493A', fg='white', text='Yes', font=("Ink Free", 13, 'bold'),
                                       relief='ridge', borderwidth=1,
                                       command=lambda: [f() for f in [ask_windows.destroy(), mcdonalds_full_frame()]])
                yes_button.place(relx=0.1, rely=0.81, relheight=0.08, relwidth=0.28)

            ask_windows.resizable(False,False)
    firstframe.mainloop()

root.resizable(False, False)
root.mainloop()
