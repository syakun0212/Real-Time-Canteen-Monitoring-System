import tkinter as tk
from tkinter import messagebox

def calculatetimewindow(): #creates a window with an entry box, labels and button (Shannon)
    window = tk.Tk()
    window.title("Waiting Time")#title of the windlw
    window.geometry("+350+70") #dimension of the window

    canvas1 = tk.Canvas(window, width=350, height=200,background='white')
    canvas1.pack()

    title1 = tk.Label(window, text='How many people are there in front of you?:',background='white')
    title1.config(font=("Calibri",12,"bold"))
    canvas1.create_window(175,30,window=title1)

    entry1 = tk.Entry(window,background='#d3d3d3')
    canvas1.create_window(175, 80, window=entry1)

    button1 = tk.Button(window,text='Get Estimated Time', command=lambda:calculatetime(3),bg='orange',
                        fg='white', relief='ridge', borderwidth=1)
    canvas1.create_window(175, 115, window=button1)

    def calculatetime(time_person): #takes user input from entry box 
                                    #applies formula to display estimated waiting time (Shannon)
      nolabel=tk.Label(window,text=" ",background='white')
      nolabel.configure(width=30)
      canvas1.create_window(150,150,window=nolabel)
      number = True
      while number == True:
        try:                                   #exception handling to catch ValueError when user inputs non-number
          people = int(entry1.get())
          if people>=0 and people<51:           #set a appropriate range of number that the user can input if not the number of people are infinite
              wait_time = people*time_person
              wait = tk.Label(window, text=wait_time,background="white")
              if wait_time < 60:
                   canvas1.create_window(150,150,window=wait)
                   labelmins = tk.Label(window, text="minutes",background="white")
                   labelmins.config(width=6)
                   canvas1.create_window(180,150,window=labelmins)
              else:
                   waithour = int(wait_time // 60)                          #convert display to minutes and hours when the time exceeds 60 minutes
                   waitmins = int((float(wait_time / 60) - waithour) * 60)
                   waithour1 = tk.Label(window, text=waithour, background='white')
                   waitmins1 = tk.Label(window, text=waitmins, background='white')
                   canvas1.create_window(125, 150, window=waithour1)
                   canvas1.create_window(180, 150, window=waitmins1)
                   labelhours = tk.Label(window, text="hour(s)", background='white')
                   labelhours.config(width=6)
                   canvas1.create_window(150, 150, window=labelhours)
                   labelmins1 = tk.Label(window, text="min(s)", background='white')
                   canvas1.create_window(207, 150, window=labelmins1)

              number = False
          else:
              error1 = messagebox.showerror("Error Message","Number out of range! Please try again.",parent=window)
              entry1.delete(0,tk.END)
              break

        except ValueError:
          error2 = messagebox.showerror("Error Message","Please enter a number!",parent=window)
          entry1.delete(0, tk.END)
          break

    window.resizable(False, False)
    window.mainloop()