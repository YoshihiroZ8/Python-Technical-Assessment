#task Loops practice
print("---Printing Numbers 1 to 10 ---")

for i in range(1, 11):
    print(i)

#Task 2: Calculate the sum of numbers in a list using a for loop 
print("\n---Calculating the sum of numbers in a list---")

numbers = [10, 20, 30, 40, 51]
total_sum = 0 

#Iterate through each number in the list 
for number in numbers:
    total_sum = total_sum + number

print(f"The list is: {numbers}")
print(f"The sum of numbers in the list is: {total_sum}")

#---Task 3 
print("\n---Input Loop with 'quit'---")
word = "python"
user_guess = ""  #input by user

while user_guess.lower() != word:
    user_guess = input("Guess the word (or type 'quit' to exit): ")
    if user_guess.lower() == 'quit':
        print("Exiting the game.")
        break

    if user_guess.lower() == word:
        print("Congratulations! You guessed the word correctly.")
    else:
        print("Incorrect guess. Try again.")

print(f"\n---Demonstrating 'Continue'---")

for j in range(1, 6):
    if j == 3:
        print("Skipping 3...")
        continue 
    print(f"Current Numebr: {j}")

print("Loop Finished.")