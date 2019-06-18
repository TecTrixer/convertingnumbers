from tkinter import *
clicked = False
def click():
    if clicked == False:
        Label(screen, text= "Clicked")
    else:
        Label(screen, text= "Unclicked")
screen = Tk()
screen.title("Converting Numbers")
Label(screen, text="Welcome to this program").pack()
Button(screen, text="Press Me", command=click).pack(fill=BOTH)
screen.mainloop()