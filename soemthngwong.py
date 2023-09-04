import pyautogui
import pyautogui as pag

import keyboard
width,height=(pag.size())

ame=True
sensitivity=0.02
increase=50
program=True
center_width,center_height=width/2,height/2
pag.moveTo(center_width,center_height, duration = sensitivity)

while program:
    if keyboard.is_pressed("Up"):
        center_height-=increase
        pag.moveTo(center_width,center_height, duration = sensitivity)
    if keyboard.is_pressed("Down"):
        center_height+=increase
        pag.moveTo(center_width,center_height, duration = sensitivity)
    if keyboard.is_pressed("Right"):
        center_width+=increase
        pag.moveTo(center_width,center_height, duration = sensitivity)
    if keyboard.is_pressed("Left"):
        center_width-=increase
        pag.moveTo(center_width,center_height, duration = sensitivity)

    if keyboard.is_pressed("Enter"):
        pag.click()
    if keyboard.is_pressed("Escape"):
        program=False





