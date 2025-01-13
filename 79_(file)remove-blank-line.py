try:
    with open("output.txt", "r") as file:
        lines = file.readlines()

    with open("output_no_blank_lines.txt", "w") as new_file:
        for line in lines:
            if line.strip():  # Only write non-blank lines
                new_file.write(line)

    print("Blank lines removed.")
except FileNotFoundError:
    print("File not found!")





















    
# Explanation:

# line.strip() removes any leading/trailing whitespace. 
# If the line is not blank, it gets written to the new file.