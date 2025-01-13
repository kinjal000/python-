try:
    with open("output.txt", "r") as file:
        lines = file.readlines()
    print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found!")


























    
# Explanation:

# file.readlines() reads the file and splits it into lines.
# len() is used to count how many lines are in the file.