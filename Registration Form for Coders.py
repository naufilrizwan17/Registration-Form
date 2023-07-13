import tkinter as tk
from tkinter import*
import re

reg = tk.Tk()
reg.title("Registration Form for Coders")
reg.geometry('500x300')
reg.configure(bg="white")

canvas_1 = tk.Canvas(reg, width=500, height=500, bg="grey")
canvas_1.pack()

label_1 = tk.Label(reg, text="Registration Form for Coders ")
label_1.configure(fg="black", font=("times", 50, 'bold'))
label_1.place(x=150, y=5)

label_2 = tk.Label(reg, text="Full Name: ")
label_2.configure(fg="black", font=("arial", 15))
label_2.place(x=50, y=80)

entry_1 = Entry(reg)
entry_1.configure(width=25, font=("arial", 8))
entry_1.place(x=150, y=90)

label_3 = tk.Label(reg, text="Email: ", )
label_3.configure(fg="black", font=("arial", 15))
label_3.place(x=50, y=120)

entry_2 = Entry(reg)
entry_2.configure(width=25, font=("arial", 8))
entry_2.place(x=150, y=130)

label_4 = tk.Label(reg, text="Gender: ")
label_4.configure(fg="black", font=("arial", 15))
label_4.place(x=50, y=160)

b = IntVar()

Radiobutton(reg, text="Male", padx=10, variable=b, value=1).place(x=140, y=170)
Radiobutton(reg, text="Female", padx=10, variable=b, value=2).place(x=200, y=170)

label_5 = tk.Label(reg, text="Country: ")
label_5.configure(fg="black", font=("arial", 15))
label_5.place(x=50, y=200)

list_of_country = ["Australia", "Afghanistan", "Belgium", "Bangladesh", "Brazil", "Canada", "England", "Germany", "Indonesia", "Iran",
                   "India", "Pakistan", "Portugal", "Russia", "Spain", "Sri Lanka", "South Africa", "USA", "Vietnam", "Zimbabwe"]

c = StringVar()

droplist = OptionMenu(reg, c, *list_of_country)
droplist.configure(width=25)
c.set('Select your Country')
droplist.place(x=150, y=200)

label_6 = tk.Label(reg, text="Age: ")
label_6.configure(fg="black", font=("arial", 15))
label_6.place(x=50, y=240)

d = IntVar()

Checkbutton(reg, text="Below 18", variable=d).place(x=120, y=250)

e = IntVar()

Checkbutton(reg, text="Above 18", variable=e).place(x=200, y=250)

label_7 = tk.Label(reg , text="Programming Language(s): ")
label_7.configure(fg="black", font=("arial", 15))
label_7.place(x=50, y=280)

entry_3 = Entry(reg)
entry_3.configure(width=45, font=("arial", 8))
entry_3.place(x=300, y=290)

label_8 = tk.Label(reg, text= "Hobbies and Interests: ")
label_8.configure(fg="black", font=("arial", 15))
label_8.place(x=50, y=320)

entry_4 = Entry(reg)
entry_4.configure(width=45, font=("arial", 8))
entry_4.place(x=250, y=330)

def click_Button():
    my_click = tk.Label(reg,text="Thank you for your time!",font=("arial",20),bg="blue",fg="black")
    my_click.pack()

Button(reg, text="Submit", bg="red", fg="black", width=15, font=("geneva", 25), command=click_Button).place(x=50, y=380)

reg.mainloop()