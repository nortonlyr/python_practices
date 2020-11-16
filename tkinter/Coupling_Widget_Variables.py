import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # create the application variable
        self.contents = tk.StringVar()

        # set it to some value
        self.contents.set('this is a variable')
        # tell the entry widget to watch this variable
        self.entrythingy['textvariable'] = self.contents

        # define a callback for when the user this return.
        # it prints the current value of the variable
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self,event):
        print('Hi. The current entry content is:', self.contents.get())