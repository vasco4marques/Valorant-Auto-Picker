
from pynput.mouse import Button, Controller
mouse = Controller()
button=Button.left
import keyboard
import cv2
import pyautogui
import numpy as np



# This are the coordinates of this agents in the 1280*960 in-game resolution    
jett=(444,794)
raze=(833,792)
reyna=(909,793)
skye=(442,868)

selectedAgent=jett

confirmButton=(643,668)

# Scale Test - Worked IG
# confirmButton=((643*1920)/1280,(668*960)/1080)

currentRes="1280x960"


        
def click_pynput(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left)
    

while True:
    print("Waitting for alt gr")
    keyboard.wait("alt gr")
    print("Got it")
    stop = True
    while stop:
        print("Moving mouse")
        click_pynput(selectedAgent[0],selectedAgent[1])
        click_pynput(confirmButton[0],confirmButton[1])
        if keyboard.is_pressed("left ctrl"):
            print("clicked")
            stop=False;
        else:
            print("No alt gr clicked")







    
    







