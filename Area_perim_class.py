class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

# Example usage:
# Create a Rectangle object
rectangle = Rectangle(10, 5)

# Call the area method
print("Area of Rectangle:", rectangle.area())  # 10 * 5 = 50

# Call the perimeter method
print("Perimeter of Rectangle:", rectangle.perimeter())  # 2 * (10 + 5) = 30
