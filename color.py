def getColor(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('pink')
        else:
            colorArray.append('light blue')
        if i == tail:
            colorArray[i] = 'cyan'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'
    return colorArray