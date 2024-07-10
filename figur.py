class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.filled = False
        self.__sides = self.__validate_sides(sides)
        self.__color = self.__validate_color(color)

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def __validate_color(self, color):
        if len(color) != 3 or not all(isinstance(x, int) for x in color):
            raise ValueError("Invalid color. Must be a list of 3 integers (RGB) between 0 and 255.")
        return color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def __validate_sides(self, sides):
        if not self.__is_valid_sides(*sides):
            return [6] * self.sides_count
        return sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):
        return 3.14159 * self.__radius * self.__radius

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        # Implement your height calculation logic here
        pass

    def get_square(self):
        # Implement your square calculation logic here
        pass

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__sides = [side] * self.sides_count

    def get_volume(self):
        return self.__sides[0] * self.__sides[0] * self.__sides[0]


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

