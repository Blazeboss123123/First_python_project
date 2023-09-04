# importing the GUI modules
from tkinter import *
from PIL import Image, ImageTk

# making and Tk window
aroot = Tk(className="THE CLICKER")
aroot.geometry("700x700")
load = Image.open("mountain.jpg")
image_back = ImageTk.PhotoImage(load)
label1 = Label(aroot, image=image_back)
label1.pack(fill=BOTH, expand=1)


class gamewindow:
    # seperating the counter window and the class window in different classes
    def __init__(self, root, allpurchases, counter=1):
        # initlizaing all the variables
        self.allpurchases = allpurchases
        self.counter = counter
        self.root = root
        self.int_entry = IntVar()

    # class function to increase the counter number everytime the button is clicked
    def add(self):
        print(self.counter)
        x = self.int_entry.get() + self.counter
        self.int_entry.set(x)
        label.config(text=self.int_entry.get())
        alert.config(text="")
        print(x)


# inherting from superclass
class shopwindow(gamewindow):
    def __init__(self, counter=1):
        # inherting the superclass variables
        super().__init__(aroot, allpurchases, counter)
        self.allpurchases = allpurchases
        self.counter = counter

    # Function to make all the buttons that are going to be in the shop window
    def button_maker(self, cost):

        buttons = []
        buttonNumber = 0
        # using iteration to make the buttons column by column
        for rows in range(len(cost)):
            b = Button(shopframe, text=f"COST: {cost[rows][0]}",
                       command=lambda a=buttonNumber: self.checkerbuy(a, buttons, cost))

            b.grid(row=rows, column=1, pady=2)
            buttons.append(b)
            buttonNumber += 1

    # function to check once button is pressed if the player can afford the button
    def checkerbuy(self, command, buttons, cost):
        def destroy(e):
            e.destroy()

        if game.int_entry.get() >= cost[command][0]:
            new_int = game.int_entry.get() - cost[command][0]
            label.config(text=new_int)
            game.int_entry.set(new_int)
            destroy(buttons[command])
            self.allpurchases = self.allpurchases[command:]
            game.counter = cost[command][2] + game.counter
            alert.config(text=cost[command][1])
        else:
            alert.config(text="𝐧𝐨𝐭 𝐞𝐧𝐨𝐮𝐠𝐡 𝐜𝐥𝐢𝐜𝐤𝐬!!")


canvas1 = Canvas(label1, width=140, height=60)
canvas1.pack()
# Creating an input box for the user to input their username

allpurchases = [[20, "You bought the double clicker!", 1], [50, "You bought the Triple clicker!", 2],
                [100, "You bought the amazing clicker!!!!", 2], [300, "You bought the X clicker", 3],
                [800, "You bought the insane clicker!!!", 5], [1100, "You bought the something amazing", 5],
                [1850, "You bought a really good clicker you should try using it!", 7],
                [2250, "You bought the powerful amazing super clicker!", 10]]


def something():
    global new
    new = entry1.get()
    file_putter()


def file_putter():
    global allpurchases, addcounter

    with open("saves_database.txt", "r+") as f:
        x = f.readlines()
        inputed = entry1.get()
        found = False
        count = 1
        for line in x:
            info = line.split(",")
            if inputed == info[0]:
                print(
                    "SAVE FILE FOUND")
                found = True
                #loading all the data of gameplay on to a save file
                buttonamount = int(info[1])
                totalbuttons: int = len(allpurchases) - buttonamount
                allpurchases = allpurchases[totalbuttons:]
                shop.button_maker(allpurchases)
                game.int_entry.set(int(info[2]))
                game.counter = int(info[3])
                alert.config(text="Save data found!")
                break
                # problems with shop buttons not decreasing and addcounter not saving
        if found == False:
            print("save file created")
            count += 1
            file = open("saves_database.txt", "a")
            file.writelines(f"{str(inputed)},{len(allpurchases)},{game.int_entry.get()},{game.counter}\n")
            file.close()

            buttons.destroy(), entry1.destroy(), canvas1.destroy()
            shop.button_maker(allpurchases)

    buttons.destroy(), entry1.destroy(), canvas1.destroy()


def exit_save():
    notfound = 0
    try:
        print(f"User: {new} is now exiting")
    except:
        print("exiting")
        aroot.destroy()
    with open("saves_database.txt", "r+") as openfile:

        file = openfile.readlines()

        for x in file:
            info = x.split(",")
            if new == info[0]:
                del file[notfound]
                with open("saves_database.txt", "w") as openfile:
                    for lines in file:
                        openfile.write(lines)
                    openfile.writelines(f"{str(new)},{len(allpurchases)},{game.int_entry.get()},{game.counter}\n")
                    aroot.destroy()
            else:
                notfound += 1


# iterates the backround colours
class backround_iterator:
    def __init__(self, colours_list):
        self.colours_list = colours_list

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        x = self.iter
        self.iter += 1
        if self.iter == len(self.colours_list):
            self.iter = 0
        return self.colours_list[x]


# all the backround colours it iterates through
changed_backround = backround_iterator(["pink", "green", "cyan", "blue", "black"])
iterator = iter(changed_backround)


def changer():
    # function to call the class
    x = next(changed_backround)
    aroot.config(bg=x)
    return aroot

entry1 = Entry(aroot)
canvas1.create_window(70, 20, window=entry1)
# running once file interpreter has read it

# making class variables
game = gamewindow(aroot, allpurchases)
shop = shopwindow()

buttonnum = len(allpurchases)
buttons = Button(text="Enter Save File Name \n or \n Create One:", command=something)
canvas1.create_window(70, 70, window=buttons)

# Adding button for counter

turn_on = Button(label1,
                 text="CLICK ME",
                 font=("Arial", 20),
                 command=game.add,
                 pady=100,
                 padx=50,
                 )
turn_on.pack(pady=50)
exits = Button(aroot, text="EXIT", font=("Arial", 13), command=exit_save)
exits.pack(side=BOTTOM, pady=60)
# visualzation of the button shown once clicked
label = Label(aroot,
              text=game.int_entry.get(),
              font=("Arial", 30)
              )
label.pack()
# packing all the variables so they are shown onto the Tk window
# shop making process
shopframe = LabelFrame(aroot, text="SHOP\n buy:")
shopframe.place(anchor=E, relx=1, rely=0.5)
# Making an exit button to close the window and end the program

# Used to tell the player what they have bought or if they do not have enough clicks
alert = Label(aroot, text="", font=("Arial", 12), bg="skyblue")
alert.pack(side=BOTTOM, pady=60)
# button to change the backround
backround = Button(aroot, text="Change backround", font=("Arial", 7), command=changer)
backround.place(anchor=NW)
# looping the whole thing so it keeps running
aroot.mainloop()
