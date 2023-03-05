import pyautogui as ap
import time

while True:
    x, y = ap.position()
    print("Mouse position: ({},{})".format(x,y))

    time.sleep(1)
