import os

def containsNumberText():
    # Open input file.
    f = open("input.txt", "r")
    NUMBERS = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    # Result variables.
    result1 = 0
    result2 = 0

    # Find calibration values.
    for x in f:

        stripped = x.strip()
    
        # Holds result for each line in part 1.
        tempResult1 = ''
        tempResult2 = ''

        # Set index to 0.
        index = 0

        # Loop through each text value from left to right.
        while index < len(stripped):
            if stripped[index].isdigit():
                tempResult1 += stripped[index]
                i = 0
                while i <= index:
                    for value in NUMBERS.keys():
                        if value in stripped[0:i]:
                            tempResult2 += NUMBERS.get(value)
                            break
                    if len(tempResult2) != 0:
                        break
                    else:
                        i += 1

                if len(tempResult2) == 0:
                    tempResult2 += stripped[index]
                break
            index += 1

        # Set index to length of string to find the second value.
        index = len(stripped) - 1

        # Loop through each text value from right to left.
        while index >= 0:
            if stripped[index].isdigit():
                tempResult1 += stripped[index]
                i = len(stripped)-1
                while i >= index:
                    for value in NUMBERS.keys():
                        if value in stripped[i:]:
                            tempResult2 += NUMBERS.get(value)
                            break
                    if len(tempResult2) >= 2:
                        break
                    else:
                        i -= 1

                if len(tempResult2) < 2:
                    tempResult2 += stripped[index]
                break
            index -= 1

        result1 += int(tempResult1)
        result2 += int(tempResult2)

    print("Part 1 answer: " + str(result1) + "\nPart 2 answer: " + str(result2))

if __name__=='__main__':
    # Run this script under this directory with the input file.
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    containsNumberText()