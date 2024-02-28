from tkinter import *

click_count = 0

def btn_click():
    global click_count
    click_count += 1
    print("Number of clicks:", click_count)

window = Tk()

btn = Button(window, text="Click me!", command=btn_click)
btn.pack()

window.mainloop()
