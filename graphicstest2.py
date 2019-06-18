from tkinter import * 
from tkinter import filedialog
from PIL import *

class MyFirstGUI:

    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable = self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.grid(columnspan=2)

        self.greet_button = Button(self.master, text="Greet", command=self.greet)
        self.greet_button.grid(row=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)
        self.label_text.set(self.LABEL_TEXT[self.label_index])
class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        self.close_text = Text(master)
        self.close_text.bind("<Button-1>", self.close)
        
        #Insert Image

        yourImage=filedialog.askopenfilename(title = "Select your image",filetypes = [("Image Files","*.gif")])
        #try:
        imgFile=Image.open(yourImage)
        imgToInsert=ImageTk.PhotoImage(imgFile)
        #except:
            #print("Error 303")
        self.close_text.image_create("current",image=imgToInsert)

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.close_text.grid(row=3)

    def close(self, event):
        print(event)
        application.quit()

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()
