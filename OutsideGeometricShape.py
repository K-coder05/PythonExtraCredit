# PROGRAMMER: Terrence Chung

# IMPORT STATEMENTS

class OutsideGeometricShape():

    # CONSTRUCTOR
    def __init__(self, radius, line_color, fill_color):
        # RADIUS EXCEPTIONS
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Outside_Geometric_Shape.py __init__ radius - radius must be a valid integer or float.")
        if radius <= 0:
            raise ValueError("Outside_Geometric_Shape.py __init__ radius - radius must be greater than zero.")

        valid_colors = ("red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple")
        # LINE_COLOR EXCEPTIONS
        if type(line_color) is not str:
            raise TypeError("Outside_Geometric_Shape.py __init__ line_color - line color must be a valid string.")
        if line_color.lower() not in valid_colors:
            raise ValueError("Outside_Geometric_Shape.py __init__ line_color - line color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple).")

        # FILL_COLOR EXCEPTIONS
        if type(fill_color) is not str:
            raise TypeError("Outside_Geometric_Shape.py __init__ fill_color - fill color must be a valid string.")
        if fill_color.lower() not in valid_colors:
            raise ValueError("Outside_Geometric_Shape.py __init__ fill_color - fill color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple).")


        # INSTANCE VARIABLES
        self.__radius = radius
        self.__line_color = line_color
        self.__fill_color = fill_color

    # INSTANCE METHODS
    def get_radius(self):
        return self.__radius


    def get_line_color(self):
        return self.__line_color


    def get_fill_color(self):
        return self.__fill_color


    def set_radius(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Outside_Geometric_Shape.py set_radius radius - radius must be a valid integer or float.")
        if radius <= 0:
            raise ValueError("Outside_Geometric_Shape.py set_radius radius - radius must be greater than zero.")
        self.__radius = radius


    def set_line_color(self, line_color):
        valid_colors = ("red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple")
        if type(line_color) is not str:
            raise TypeError("Outside_Geometric_Shape.py set_line_color line_color - line color must be a valid string.")
        if line_color.lower() not in valid_colors:
            raise ValueError("Outside_Geometric_Shape.py set_line_color line_color - line color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple).")
        self.__line_color = line_color


    def set_fill_color(self, fill_color):
        valid_colors = ("red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple")
        if type(line_color) is not str:
            raise TypeError("Outside_Geometric_Shape.py set_fill_color fill_color - fill color must be a valid string.")
        if fill_color.lower() not in valid_colors:
            raise ValueError("Outside_Geometric_Shape.py set_fill_color fill_color - fill color must be a valid color (Red, White, Blue, Orange, White, Black, Green, Yellow, Purple).")
        self.__fill_color = fill_color


    def area(self):
        return Math.PI * (self.__radius ** 2)


    def perimeter(self):
        return 2 * Math.PI * self.__radius