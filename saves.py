from tkinter import *

start=Tk(className="Welcome.")
start.geometry("300x200")
start.configure(bg="skyblue")
buttons = Button(text="Login")
buttons.pack(side=BOTTOM,ipadx=70)
buttons1=Button(text="signup")
buttons1.pack(side=BOTTOM,ipadx=70)

start.mainloop()