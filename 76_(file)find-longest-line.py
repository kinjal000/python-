try:
    with open("output.txt", "r") as file:
        lines = file.readlines()
    longest_line = max(lines, key=len)
    print("Longest line:", longest_line)
except FileNotFoundError:
    print("File not found!")























    
# Explanation:

# max(lines, key=len) finds the line with the maximum length (the longest line).