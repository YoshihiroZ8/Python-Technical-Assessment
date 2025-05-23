#Task for function def practice 
def calculate_rectangle_area(length, width):
    """Calculates the area of rectangle"""
    if length < 0 or width < 0:
        print("\nWarning: Length and width should be non-negative number.")
        return None

    area = length * width
    return area

def is_prime(number):
    """Checks if the number is a prime number"""

    if number <= 1:
        return False
    
    if number <= 3:
        return False

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5

    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6 
    return True #If no divisor found, it's a prime number

#----Function to reverse the string
def reverse_string(input_string):
    """Reverses the input string"""
    # Parameter 'input_string' is local to this function.
    # String slicing [::-1] is a concise way to reverse a string in Python.
    reversed_str = input_string[::-1]
    return reversed_str

#----Calling the function and demonstrating the usage
print("\n----- Using the Functions -----")

#calling calcualte_rectangle_area function
rect_length = 10
rect_width = 5

rectangle_area = calculate_rectangle_area(rect_length, rect_width)
if rectangle_area is not None:
    print(f"The are of a reactangle with legnth {rect_length} and width {rect_width} is: {rectangle_area}")

number_check = 17
if is_prime(number_check):
    print(f"{number_check} is a prime number.")
else:
    print(f"{number_check} is not a prime number.")

number_check_2 = 15
if is_prime(number_check_2):
    print(f"{number_check_2} is a prime number.")
else:
    print(f"{number_check_2} is not a prime number.")

#calling reverse_string function
string = "Hello Python"
reversed_string = reverse_string(string)
print(f"The original is: '{string}'")
print(f"The reversed string is; '{reversed_string}'")