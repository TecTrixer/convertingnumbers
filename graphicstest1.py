from tkinter import *
class testwindow:
    def __init__():
        self.clicked = False
    def click():
        if self.clicked == False:
            Label(screen, text= "Clicked").pack()
        else:
            Label(screen, text= "Unclicked").pack()
    screen = Tk()
    screen.title("Converting Numbers")
    Label(screen, text="Welcome to this program").pack()
    Button(screen, text="Press Me", command=click).pack(fill=BOTH)
    screen.mainloop()