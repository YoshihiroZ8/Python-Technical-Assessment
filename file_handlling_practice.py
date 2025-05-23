import os

input_filename = "input.txt"
output_filename = "output.txt"

if not os.path.exists(input_filename):
    print(f"Creating sample input file: {input_filename}")
    try:
        with open(input_filename, 'w') as infile:
            infile.write("Hello, world!\n")
            infile.write("It has multitple lines.\n")
            infile.write("We will count the words in this file.\n")
        print(f"Sample file '{input_filename}' created.")
    except IOError as e:
        print(f"Error creating input file: {e}")
        exit()

else:
    print(f"Using existing input file: {input_filename}")


#----- Step 2: Read Data from the input file and count
word_count = 0 

try: 
    with open(input_filename, "r") as infile:
        print(f"\Reading from '{input_filename}'...")
        content = infile.read()

        words = content.split()

        word_count = len(words)

        print(f"Finished reading from '{input_filename}'.")
        print(f"Total words found: {word_count}")
    
except FileNotFoundError:
    print(f"Error: The file '{input_filename}': {e}")
except IOError as e:
    print(f"Error reading from '{input_filename}': {e}")
except Exception as e:
    print(f"An unexpected error occurred during reading: {e}")


#Step 3: write the word count to the output file
if word_count > 0:
    try:
        with oen(output_filename, "w") as outfile:
            print(f"\nWriting word count to '{output_filename}'...")
            outfile.write(f"Total words in {input_filename} is: {word_count}\n")
            print(f"Word count successfully written to '{output_filename}'.")

    except IOError as e:
        print(f"Error writing to '{output_filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred during writing: {e}")

else:
    print("\nCould not calculate word count, skipping writing to output file.")