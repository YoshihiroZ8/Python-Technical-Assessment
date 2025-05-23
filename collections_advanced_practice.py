from collections import Counter
import re 

input_filename = "input.txt"

content = ""
try:
    with open(input_filename, "r") as infile:
        print(f"Raading from '{input_filename}'...")
        content = infile.read()
        print(f"Finished reading from '{input_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    exit()
except IOError:
    print(f"Error reading form '{input_filename}': {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred during reading: {e}")
    exit()


#---step 2
if content:
    print("\nCounting word frequencies...")

    content = content.lower()

    words = re.findall(r'\b\w+\b', content)

    word_counts = Counter(words)

    print("Word Frequency Count Complete: ")

    #---Step 3: Print the word frequencies
    print("\n---Word Frequencies ---")
    for word, count in word_counts.items():
        print(f"'{word}': {count}")

else:
    print("No content read form the file.")


# -----Optional: Demostrate defaultdict and deque basics 

print("\n ---Basic Defaultdict Example ---")

print("\n ---Basic Deque Example ---")
from collections import deque

my_deque = deque([1, 2, 3])
print(f"Initial deque: {my_deque}")

#add to the right
my_deque.append(4)
print(f"after append(4): {my_deque}")

#add to the left
my_deque.appendleft(0)
print(f"After appendleft(0): {my_deque}")

#Remove from the right
popped_right = my_deque.pop()
print(f"After pop(): {my_deque}, popped value: {popped_right}")

#Remove from the left
popped_left = my_deque.popleft()
print(f"After popleft(): {my_deque}, popped value: {popped_left}")


