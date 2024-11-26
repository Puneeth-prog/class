class Circle:
    def __init__(self, a):
        self.a = a  # Store the value of 'a' in an attribute, though it’s not used directly here
        self.numbers = [10, 501, 22, 37,100,999,87,351]  # Define a list inside the class

    def add_numbers(self):
        # Access the 2nd and 4th elements from the list (index 1 and 3)
        return self.numbers[1] + self.numbers[3]

# Create an instance of the Circle class
circle_obj = Circle(10)  # The argument '10' is not used directly in this case

# Call the add_numbers method on the object
result = circle_obj.add_numbers()
print(result)
