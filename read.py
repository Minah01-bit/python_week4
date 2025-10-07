# File Read & Write Challenge 🖋️
# Error Handling Lab 🧪

def modify_file_content(text):
    """
    Modify the file content in some way.
    For example, convert it to uppercase.
    """
    return text.upper()  # You can change this logic if you like


def process_file():
    # Ask the user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write the modified version to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don’t have rights to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
process_file()
