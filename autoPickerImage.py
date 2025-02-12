from pynput.mouse import Button, Controller
mouse = Controller()
button=Button.left
import keyboard
import cv2
import pyautogui
import numpy as np


def click_pynput(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left)
    

template = cv2.imread("agents/jett.png", cv2.IMREAD_UNCHANGED)
stop = True
while stop:

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)  # Convert to NumPy array
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Convert color format

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    threshold = 0.8  # Confidence level
    if max_val >= threshold:
        target_x = max_loc[0] + template.shape[1] // 2
        target_y = max_loc[1] + template.shape[0] // 2
        click_pynput(target_x, target_y)
        

        stop = False
    else:
        print("Agent not found")