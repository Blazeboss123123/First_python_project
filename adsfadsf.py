
from tkinter import *
import time
from tkinter.ttk import Labelframe



class gamewindow:

    def __init__(self,root,counter):
        self.root = root
        self.int_entry = IntVar()
        self.counter = counter

    def add(self):

        x = self.int_entry.get() + self.counter
        self.int_entry.set(x)
        label.config(text=self.int_entry.get())

        return self.int_entry.set(x)


class shopwindow(gamewindow):
    def __init__(self,firstbuy,counter):
        super().__init__(aroot,1)
        self.counter = counter
        self.firstbuy=firstbuy


    def button_maker(self):

    def checkerbuy(self):

        if self.int_entry.get() <= self.firstbuy:
            alert.config(text="Not enough money")
            print(self.int_entry.get())




        else:
            alert.config(text="")
            self.int_entry.get()-self.firstbuy


if __name__ == "__main__":
    aroot = Tk(className="THE CLICKER")
    aroot.geometry("500x500")
    aroot.configure(bg="skyblue")

    game=gamewindow(aroot,counter=1)
    shop=shopwindow([20,100],[2,4])
    turn_on = Button(aroot,
                     text="CLICK ME",
                     font=("Arial",20),
                     command=game.add,
                     )

    label = Label(aroot,
                  text = game.int_entry.get(),
                  font=("Arial",10)
                  )

    shopframe=Labelframe(aroot,text="SHOP\n buy:")
    shopframe.pack(side=RIGHT,ipady=300,ipadx=20)

    buy1=Button(shopframe,text=f"double clicker {shop.firstbuy}",command=shop.checkerbuy)
    buy1.grid(row=1,column=1)

    alert=Label(aroot,text="",bg="skyblue")
    alert.pack(side=BOTTOM)

    turn_on.pack()
    label.pack()
    aroot.mainloop()



