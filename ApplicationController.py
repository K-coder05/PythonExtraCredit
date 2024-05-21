# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
import tkinter
import pickle
import json

class ApplicationController():
    # CONSTRUCTOR
    def __init__(self, model_outside, model_inside, view):
        self.__default_circle_radius = 10.0
        self.__default_circle_line_color = "black"
        self.__default_circle_fill_color = "red"        
        
        self.__default_rectangle_length = 10.0
        self.__default_rectangle_height = 20.0
        self.__default_rectangle_line_color = "black"
        self.__default_rectangle_fill_color = "red"        
        
        self.__model_outside = model_outside
        self.__model_inside = model_inside
        self.__view = view        
        
        self.__application_window = self.__view.get_application_window()
        
        self.__application_menu = tkinter.Menu(self.__application_window)
        
        # File menu
        self.__file_menu = tkinter.Menu(self.__application_menu)
        self.__file_menu.add_command(label="New", command=self.file_new)
        self.__file_menu.add_command(label="Open", command=self.file_open)
        self.__file_menu.add_command(label="Save as XML")
        self.__file_menu.add_command(label="Save as JSON")
        self.__application_menu.add_cascade(label="File", menu=self.__file_menu)
        
        # Edit Menu
        self.__edit_menu = tkinter.Menu(self.__application_menu)
        self.__edit_menu.add_command(label="Outside Shape (Circle) Radius")
        self.__edit_menu.add_command(label="Outside Shape (Circle) Line Color")
        self.__edit_menu.add_command(label="Outside Shape (Circle) Fill Color")
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Length")
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Height")
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Line Color")
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Fill Color")
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Radius")
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Line Color")
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Fill Color")
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Length")
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Height")
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Line Color")
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Fill Color")
        self.__application_menu.add_cascade(label="Edit", menu=self.__edit_menu)        
        
        # View Menu
        self.__view_menu = tkinter.Menu(self.__application_menu)
        self.__view_menu.add_command(label="Outside Geometric Shape", command=self.view_outside_shape) # Circle
        self.__view_menu.add_command(label="Inside Geometric Shape", command=self.view_inside_shape) # Rectangle
        self.__application_menu.add_cascade(label="View", menu=self.__view_menu)
        
        # Help Menu
        self.__help_menu = tkinter.Menu(self.__application_menu)
        self.__help_menu.add_command(label="About", command=self.__view.get_about)
        self.__application_menu.add_cascade(label="Help", menu=self.__help_menu)
        
        self.__application_window["menu"] = self.__application_menu
        self.__application_window.mainloop()
        
    # INSTANCE METHODS
    def file_new(self):
        
        # Initialize default values for pickle file for outside shape (circle)
        circle_settings = (self.__default_circle_radius, self.__default_circle_line_color, self.__default_circle_fill_color)
        
        with open("OutsideShape.pickle", "wb") as binary_file_input:
            pickle.dump(circle_settings, binary_file_input)
        
        # Initialize default values and pickle file for inside shape (rectangle)
        rectangle_settings = (self.__default_rectangle_length, self.__default_rectangle_height, self.__default_rectangle_line_color, self.__default_rectangle_fill_color)
        
        with open("InsideShape.pickle", "wb") as binary_file_input:
            pickle.dump(rectangle_settings, binary_file_input)
    
    def file_open(self):
        self.__json_values = { 
            "outside_shape" : {},
            "inside_shape" : {}
        }
        
        self.__json_values["outside_shape"]["radius"] = self.__model_outside.get_radius()
        self.__json_values["outside_shape"]["line_color"] = self.__model_outside.get_line_color()
        self.__json_values["outside_shape"]["fill_color"] = self.__model_outside.get_fill_color()
        
        self.__json_values["inside_shape"]["length"] = self.__model_inside.get_length()
        self.__json_values["inside_shape"]["height"] = self.__model_inside.get_height()
        self.__json_values["inside_shape"]["line_color"] = self.__model_inside.get_line_color()
        self.__json_values["inside_shape"]["fill_color"] = self.__model_inside.get_fill_color()
        
        save_file = open("applicationdata.sjon", "w")
        json.dump(self.__json_values, save_file, indent = 6)
        save_file.close()
        
        # UPDATE (Open the JSON file)
    
    def file_save_xml(self):
        pass
    
    def file_save_json(self):
        pass
    
    def view_outside_shape(self):
        self.__temp_application_window = tkinter.Tk()
        self.__temp_application_window.title("Outside Shape")
        self.__temp_application_window.geometry("800x500")
        
        self.__temp_application_window.mainloop()
        
    def view_inside_shape(self):
        self.__temp_application_window = tkinter.Tk()
        self.__temp_application_window.title("Inside Shape")
        self.__temp_application_window.geometry("800x500")
        
        self.__temp_application_window.mainloop()