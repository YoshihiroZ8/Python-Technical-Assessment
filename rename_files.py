import os

def rename_files_in_directory(directory_path, old_text, new_text):
    """Renames files in a directory by replacing old_text with new_text in their names. """
    try:
        for count, filename in enumerate(os.listdir(directory_path)):
            if old_text in filename:
                src = os.path.join(directory_path, filename)
                dst_filename = filename.replace(old_text, new_text)
                dst = os.path.join(directory_patj, dst_filename)

                #rename the file
                os.rename(src, dst)
                print(f"Renamed: {filename} to {dst_filename}")
            else:
                print(f'Skipped: {filename}" as it does not contain the "{old_text}"')
        print("\nFile renaming process completed.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#---Configuration ---
TARGET_DIRECTORY = r"C:\Users\User\Python" 

OLD_SUBSTRING = "old_prefix"

NEW_SUBSTRING = "new_prefix"

#---main execution ---
if __name__ == "__main__":
    if TARGET_DIRECTORY == r"C:\Users\User\Python":
        print("Please update the TARGET_DIRECTORY variable in the script with the actual path to your files.")
    else:
        print(f"Starting to rename files in: {TARGET_DIRECTORY}")
        print(f"Replacing instances of '{OLD_SUBSTRING}' with '{NEW_SUBSTRING}'.\n")
        rename_files_in_directory(TARGET_DIRECTORY, OLD_SUBSTRING, NEW_SUBSTRING)
