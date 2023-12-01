import os

# Run this script under this directory with the input file.
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Open input file.
f = open("input.txt", "r")

# Result variable.
result = 0

# Find calibration values.
for x in f:
    tempResult = ''
    # Strip the endline from each line.
    stripped = x.strip()
    index = 0
    while index < len(stripped):
        if stripped[index].isdigit():
            tempResult += stripped[index]
            break
        index += 1
    index = len(stripped) - 1
    while index >= 0:
        if stripped[index].isdigit():
            tempResult += stripped[index]
            break
        index -= 1
    result += int(tempResult)

print("Part 1 answer: " + str(result))