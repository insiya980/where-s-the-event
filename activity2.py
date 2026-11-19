from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
def message():
    messagebox.showwarning("Warning","This is a warning message")
button=Button(window,text="Alert",command=message)
button.place(x=40,y=80)
window.mainloop()