class Circle:
    # Private class variable (constant)
    _pi = 3.14  # Class variable (usually denoted as a private member)

    def __init__(self, radius):
        self.radius = radius  # Instance variable (specific to each object)

    def area(self):
        """Calculate the area of the circle using the constant pi."""
        return Circle._pi * self.radius ** 2  # Use the class variable _pi

    def perimeter(self):
        """Calculate the circumference (perimeter) of the circle using the constant pi."""
        return 2 * Circle._pi * self.radius  # Use the class variable _pi

# Example usage:
# Create a Circle object
circle = Circle(7)

# Call the area method
print("Area of Circle:", circle.area())  # π * 7^2 = 3.14 * 49 = 153.86

# Call the perimeter (circumference) method
print("Perimeter (Circumference) of Circle:", circle.perimeter())  # 2 * π * 7 = 2 * 3.14 * 7 = 43.96
