import tkinter as tk
import tkinter.messagebox as mbox
import pyautogui

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")

        self.label = tk.Label(master, text="Click the button to take a screenshot.")
        self.label.pack()

        self.button = tk.Button(master, text="Take Screenshot", command=self.take_screenshot)
        self.button.pack()

    def take_screenshot(self):
        # Hide the main window so it doesn't appear in the screenshot
        self.master.withdraw()

        # Wait a short time for the window to be hidden
        self.master.after(100)

        # Take the screenshot and save it to a file
        left = 0
        top = 0
        width = 1200
        height = 500
        
        screenshot = pyautogui.screenshot(region=(left,top,width, height))
        screenshot.save(r'C:\Users\Owner\Desktop\programming\Python\tkinter\screenshot.png')

        # Show a message box to confirm that the screenshot was taken
        mbox.showinfo("Screenshot Taken", "The screenshot has been saved to screenshot.png")

        # Show the main window again
        self.master.deiconify()

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
