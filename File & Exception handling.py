# QN.1 File Read & Write Challenge
def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: {input_filename} does not exist.")
    except IOError:
        print("Error: Issue with reading or writing the file.")

       
 #QN.2 Error Handling Lab
def read_file_with_error_handling():
    input_filename = input("Enter the filename: ")
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
    except PermissionError:
        print(f"Error: No permission to read {input_filename}.")
    except IOError:
        print(f"Error: Problem reading {input_filename}.")
