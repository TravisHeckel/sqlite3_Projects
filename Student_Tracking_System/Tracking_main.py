#Python Version: 3.11.4

#Author: Travis Heckel

#Purpose: This will hold a list of students information and courses being taken. THis will allow for the
# modifying of this list through adding and deleting.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

#This module contains the GUI (graphic user interface)
import Tracking_GUI
#This module contains all the necessary functions for the system.
import Tracking_func

#Frame is the class that Tkinter porivdes that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #This will define our main configuration for the window that opens up
        self.master = master
        self.master.minsize(600, 400) #(Height and width)
        self.master.maxsize(600, 400)
        # This center window method will center our app on the users screen
        Tracking_func.center_window(self, 500, 300)
        self.master.title("The Student Tracking system Demo")
        self.master.configure (bg="#182A53")
        #This protocol method is a tkinter built-in method used to recognize if the user clickers the upper corner 'x' on windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: Tracking_func.ask_quit(self))
        arg = self.master

        #This loads in the widgets from a seperate module, doing this allows you to avoid long lists of code.
        Tracking_GUI.load_gui(self)

        #This creates the drop down menu  at the top of the window that is preset in tkinter.
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", underline = 1, accelerator = "Ctrl + Q", command = lambda: Tracking_func.ask_quit(self))
        menubar.add_cascade(label = "File", underline = 0, menu = filemenu)
        helpmenu = Menu (menubar, tearoff = 0) # defines the particular drop down column and tear off = 0 means do not seperate menu bar.
        helpmenu.add_separator()
        helpmenu.add_command (label = "how to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label = "About this Tracking system") #add _command is a child menu bar item of the add_cascade parent item
        menubar.add_cascade(label = "Help", menu = helpmenu) #Add _cascade si a parent menubar item (visible heading)
        
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """

        self.master.config(menu = menubar, borderwidth = "1.5")

        
        """
        It is from these few lines of code that Python will begin our gui and application
        The (if __name__ == "__main__":) part is basically telling Python that if this script
        is ran, it should start by running the code below this line....in this case we have
        instructed Python to run the following and in this order:

        root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
        App = ParentWindow(root)    #This instantiates our own class as an App object
        root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                    #meaning, it will stay open until we instruct it to close
        """
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
