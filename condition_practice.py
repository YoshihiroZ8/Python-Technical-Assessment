#If-else statement 
print ("---Checking Number ---")

# Get Number input from the user 
num_str = input("Enter a number: ")

try:
    #covert input number into float (allow decimal numbers)
    num = float(num_str)

    #use if, elif, else to check the number
    if num > 0:
        print(f"{num} is positive number.")
    elif num < 0:
        print(f"{num} is negative number.")
    else: #the only remaining case is number == 0
        print(f"{num} is zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")


#Task: Determine Voting Elighbility
print(f"Invalid input for number. Please enter a valid number.")

#Get age input to an integer
age_str = input("Enter your age: ")

try:
    age = int(age_str)

    #Define Voting age
    voting_age = 18

    #Use if and else to check voting eligibility
    if age >= voting_age:
        print(f"You are eligible to vote.")
    else:
        print(f"You are not eligible to vote yet. You need to be at least {voting_age} years old.")

except ValueError:
    print("Invalid input for age. Please enter a while number for your age.")



#Case Statement 
def handle_case_a():
    print("Case A")

def handle_case_b():
    print("Case B")

def handle_case_c():
    print("Case C")

def handle_default():
    print("Invalid case")

case_action = {
    "A": handle_case_a,
    "B": handle_case_b,
    "C": handle_case_c
}

case = input("Enter a case (A, B, or C): ")

action_to_perform = case_action.get(case, handle_default)

action_to_perform()