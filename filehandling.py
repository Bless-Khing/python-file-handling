def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Please enter the filename to read: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully.")
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename}.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: An I/O error occurred while accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to execute
read_and_modify_file()
