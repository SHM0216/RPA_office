import pyautogui


left = 0
top = 0
width = 1200
height =  500

myScreenshot = pyautogui.screenshot(region=(left, top, width, height))



myScreenshot.save(r'C:\Users\Owner\Desktop\programming\Python\pyautogui\screen shot1.png')

