class Figure:
    unit = 'cm'
    
    def __init__(self):
        pass
    
    def calculate_area(self):
        pass
    
    def info(self):
        pass    
    
class Square(Figure):
    def __init__(self,side_length):
        super().__init__()
        self.__side_length = side_length
    
    def calculate_area(self):
        return self.__side_length ** 2
    
    def info(self):
        area = self.calculate_area()
        print(f'Square side length: {self.__side_length} {Figure.unit}, area: {area} {Figure.unit}')
        
square = Square(5)
square.info()
    
class Rectangle(Figure):
    def __init__(self,length,width):
        super().__init__()
        self.__length = length
        self.__width = width
        
    def calculate_area(self):
        return self.__length * self.__width
    
    def info(self):
        area = self.calculate_area()
        print(f'Rectangle length: {self.__length} {Figure.unit}, width: {self.__width} {Figure.unit}, area: {area} {Figure.unit}')
        
rectangle = Rectangle(5,8)
rectangle.info()

square_1 = Square(8)
square_2 = Square(15)
list_squares = [square_1,square_2]

rectangle_1 = Rectangle(7,14)
rectangle_2 = Rectangle(9,18)
rectangle_3 = Rectangle(5,10)
list_rectangles = [rectangle_1,rectangle_2,rectangle_3]

figures = list_squares + list_rectangles


for figure in figures:
    figure.info()