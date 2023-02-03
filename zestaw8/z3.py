import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar

okno = tk.Tk()
okno.title("Clock and Calendar App")
okno.geometry("400x250")
okno.resizable(width=False, height=False)

date_time = StringVar()

def update_date_time():
    day = datetime.today().strftime('%d')
    month = datetime.today().strftime('%B')
    year = datetime.today().strftime('%Y')
    time = datetime.now().strftime("%H:%M:%S")
    dayOfWeek = datetime.today().strftime("%A")
    dt = day + " " + month + " " + year + "\n" + time + " " + dayOfWeek
    date_time.set(dt)
    date_time_label.after(1000, update_date_time)

date_time_label = Label(okno, textvariable=date_time, font=("Helvetica", 16), bg='dark grey', width=100)
date_time_label.pack(anchor="center")

current_time = datetime.now()
day = current_time.strftime('%d')
month = current_time.strftime('%m')
year = current_time.strftime('%Y')

cal = Calendar(okno, selectmode='day', year=int(year), month=int(month), day=int(day))
cal.pack(anchor="center")

update_date_time()
okno.mainloop()
