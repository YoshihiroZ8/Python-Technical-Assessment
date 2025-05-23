#Take input from the user
name = input("Enter your name: ")
age_str = input("Enter your age: ")

#Covert the age input from string into integer
try:
    age = int(age_str)

    print(f"Hello, {name}! You are {age} years old.")

except ValueError:
    print("Invalid input for age. Please enter a number.")
    