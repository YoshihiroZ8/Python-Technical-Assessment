#Lists
print("-----Demostrating Lists -----")

#Create a list of fruits 
fruits = ["appple", "banana", "orange", "grape", "cherry"]
print(f"initial List: {fruits}")

#add on item to the end of the list 
fruits.append("mango")
print(f"List after adding mango: {fruits}")

#add an item at a specific index
fruits.insert(1, "kiwi")
print(f"After adding 'kiwi' at index 1: {fruits}")

#remove an item by value
fruits.remove("banana")
print(f"After removing 'orange': {fruits}")

#remove the last item and get its value
popped_fruit = fruits.pop()
print(f"After popping the last item('{popped_fruit}'): {fruits}")

#remove an item by index
del fruits[0]
print(f"After deleting the item at index 0: {fruits}")

#sort the list alphabetically
fruits.sort()
print(f"After sorting the list: {fruits}")

# ---Dictionaries--- 
print("\n-----Demostrating Dictionaries-----")

#create a dictionary of contact information
contact_info = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
print(f"Initial Dictionary: {contact_info}")

#access a value using its key
print(f"Alice's phone number: {contact_info['Alice']}")

#Add a new entry
contact_info["David"] = "999-888-7777"
print(f"After adding David: {contact_info}")

#Update an existing entry
contact_info["Alice"] = "111-222-3333"
print(f"After updating Alice's number: {contact_info}")

#remove an entry by key using del
del contact_info["Charlie"]
print(f"After removing Charlie: {contact_info}")

#remove an entry by key using pop and get its value
popped_number = contact_info.pop("Bob")
print(f"After popping Bob's number('{popped_number}'): {contact_info}")

# --- Basic examples of Tuples and Sets ---
print("\n-----Basic examples of Tuples and Sets ---")

#tuples are ordered and imutable (cannot be changed after creation)
my_tuple = (1, 2, 3, "four")
print(f"Example Tuple: {my_tuple}")

# Sets are unordered collections of unique elements
my_set = {"apple", "banana", "cherry", "apple"} # Duplicate 'apple' is ignored
print(f"Example Set: {my_set}")
my_set.add("date")
print(f"Set after adding 'date': {my_set}")
my_set.remove("banana")
print(f"Set after removing 'banana': {my_set}")