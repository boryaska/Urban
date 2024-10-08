import math
class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        if isinstance(sides, (int, float)):
            self.__sides = [sides]
        else:
            self.__sides = sides
        self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for x in color:
            if x < 0 or x > 255:
                return False
        return True

    def set_color(self, *color):
        if Figure.__is_valid_color(self, color):
            self.__color = color
            
    def __is_valid_sides(self, *new_sides):
        if all(x > 0 for x in new_sides) and len(new_sides) == len(self.__sides):
            return True
        return False
    
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        return sum(self.__sides)
    
    def set_sides(self, *new_sides):
        if Figure.__is_valid_sides(self, *new_sides):
            self.__sides = list(new_sides)
            return True
        return False

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = float(sides)/(2*math.pi)

    def get_square(self):
        square = math.pi * (self.__radius ** 2)
        return square

    def set_sides(self, new_sides):
            if super().set_sides(new_sides):
                self.__radius = float(new_sides) / (2 * math.pi)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
    
    def get_square(self):
        sides = Triangle.get_sides(self)
        a, b, c = sides
        p = 0.5 * sum(sides)
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return square
        


class Cube(Figure):
    def __init__(self, color, side):
        sides = []
        for i in range(12):
            sides.append(side)
        super().__init__(color, sides)

    def get_volume(self):
        rib = (super().get_sides())[0]
        return (rib ** 3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
