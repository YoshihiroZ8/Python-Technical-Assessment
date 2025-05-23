# --- using the 'random' module
import random 

print("---Rolling a Dice ---")

dice_roll =  random.randint(1,6)
print(f"You rolled a: {dice_roll}")

#simulate picking a random element form a list
my_list = ["apple", "banana", "cherry", "date"]
random_item = random.choice(my_list)
print(f"Randomly picked from list {my_list}: {random_item}")

#--- Using the 'math' module
import math

print ("\n---Using the Math Module---")
number = 16

square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")

angle_degrees = 90

angle_radians = math.radians(angle_degrees)
since_value = math.sin(angle_radians)
print(f"The sign of {angle_degrees} degrees is: ({angle_radians:.2f} radians) is: {since_value}")

print(f"The value of pi is: {math.pi}")

# --- Using the 'request' package
import requests

print(f"---Using the Requests Package ---")
url = "https://www.example.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Successfully fetched data from {url}")

        print("Content Snippet:")
        print(response.text[:200] + "...")
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching data: {e}")