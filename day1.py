validWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
wordToIntDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }
def importFile():
    filename = "day1.txt"
    file = open(filename, 'r')
    allLines = []
    while True:
        line = file.readline()
        if not line:
            break
        allLines.append(line)
    return allLines
def wordToInt(charCat):
    charLen = len(charCat)
    for word in validWords:
        wordLen = len(word)
        if wordLen <= charLen:
            if word == charCat[charLen - wordLen:]:
                return wordToIntDict[word]
    return 'n'
def parseArray(allLines):
    numArray = []
    for value in allLines:
        firstValue = None
        lastvalue = None
        charCat = ''
        for char in value:
            charCat = charCat + char
            val = char
            wordToIntChecker = wordToInt(charCat)
            if wordToIntChecker.isdigit():
                val = wordToIntChecker
            if val.isdigit():
                if firstValue == None:
                    firstValue = val
                lastvalue = val
        numArray.append(firstValue + lastvalue)
    return numArray
def addAllValues(numArray):
    total = 0
    for value in numArray:
        total = total + int(value)
    return total
print(addAllValues(parseArray(importFile())))
print(wordToInt('eight245nine'))