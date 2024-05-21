# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
import tkinter
import tkinter.messagebox
import tkinter.simpledialog

class ApplicationView():
    # CONSTRUCTOR
    def __init__(self):
        self.__application_window = tkinter.Tk()
        self.__application_window.title("Application")
        self.__application_window.geometry("800x600")
        
    def get_application_window(self):
        return self.__application_window
    
    def get_filename(self):
        filename = tkinter.simpledialog.askstring("Filename Input", "Enter filename")
        return filename
    
    def get_about(self):
        tkinter.messagebox.showinfo("Application Extra Credit", "Spring 2024")