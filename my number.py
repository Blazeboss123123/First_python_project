#TEXT GAME
#crossy roadyy
# to make crossy road you can make a fucntion as a seperate file 
import os
import random
import time
from pynput.keyboard import *



def main_Road(road,increase=7):

    global characater,character_road
    global character_road_string
    characater="0"

    increase_x=increase-1

    increase=increase*" "

    character_increase=increase_x*" "
    roads_1=[ "| ===== |","| ===== |","| ===== |","| ===== |"]
    character_road_string=["| " ,"=","=","=","=","=" ," |"]

    for printed_road in roads_1:
        print(f"{increase}{printed_road}")

    joined="".join(character_road_string)
    print("0",character_increase,joined)
    for printed_road in roads_1:
        print(f"{increase}{printed_road}")


def car_location():
    x=random.randint(1,5)

def press_on(key):

    return True
def press_off(key):

    return False
whilegameisplayign=True


main_Road("|")
try:
    count=7
    while True:
        with Listener(on_release=press_off) as listener:
            listener.join()

            count-=1
            main_Road("|",count)
            if "0|" in character_road_string:
                pass



except:
    pass