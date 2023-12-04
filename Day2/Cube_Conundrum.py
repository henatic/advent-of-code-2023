import os

def possibleGames(lines):
    sum = 0
    BAG = {
        'red':12,
        'green':13,
        'blue':14
    }
    for x in lines:
        gameNum = int(x.strip()[5:x.index(':')])
        gameSet = x.strip()[x.index(':')+1:].split(';')
        isValid = True
        for round in gameSet:
            picks = round.split(',')
            for colors in picks:
                colorpick = colors[1:].split(' ')
                if int(colorpick[0]) > BAG.get(colorpick[1]):
                    isValid = False
                    break
                # else:
                #     print(colorpick)
        if isValid:
            sum += gameNum

    return sum

def fewestCubes(lines):
    result = 0
    for x in lines:
        BAG = {
            'red':0,
            'green':0,
            'blue':0
        }
        gameSet = x.strip()[x.index(':')+1:].split(';')
        for round in gameSet:
            picks = round.split(',')
            for colors in picks:
                colorpick = colors[1:].split(' ')
                if BAG.get(colorpick[1]) < int(colorpick[0]):
                    BAG[colorpick[1]] = int(colorpick[0])
        BAG['red'] = 1 if BAG.get('red') == 0 else BAG.get('red')
        BAG['green'] = 1 if BAG.get('green') == 0 else BAG.get('green')
        BAG['blue'] = 1 if BAG.get('blue') == 0 else BAG.get('blue')
        result += (BAG.get('red') * BAG.get('green') * BAG.get('blue'))
    return result
    

if __name__=='__main__':
    # Run this script under this directory with the input file.
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    # Get input contents and close file.
    f = open("input.txt", "r")
    input = f.readlines()
    f.close()
    print(str(possibleGames(input)))
    print(str(fewestCubes(input)))