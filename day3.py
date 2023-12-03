from enum import Enum

filename = "day3.txt"

# open file and read valuesMap into a list
allValues = []
with open(filename, "r") as file:
    valuesMap = []
    valuesMask = []
    for line in file:
        lineList = []
        lineMask = []
        for char in line.strip():
            # Process each line here
            lineList.append(char)  # Example: Print each line after stripping whitespace
            lineMask.append(0)
        valuesMap.append(lineList)
        valuesMask.append(lineMask)
#utils -----------------
def isSpecialCharacter(char):
    if char == '.':
        return False
    elif char.isdigit():
        return False
    else:
        return True
class GrowDirection(Enum):
    grow_back = 1
    grow_forward = 2
    grow_both = 3
def fetchInt(index, charIndex, grow_direction):
    if (index < 0 or index >= len(valuesMap)):
        return ''
    if (charIndex < 0 or charIndex >= len(valuesMap[index])):
        return ''
    if (valuesMap[index][charIndex].isdigit() and valuesMask[index][charIndex] == 0):
        valuesMask[index][charIndex] = 1
        if (grow_direction == GrowDirection.grow_back):
            return fetchInt(index, charIndex-1, grow_direction) + valuesMap[index][charIndex]
        elif (grow_direction == GrowDirection.grow_forward):
            return valuesMap[index][charIndex] + fetchInt(index, charIndex+1, grow_direction)
        elif (grow_direction == GrowDirection.grow_both):
            return fetchInt(index, charIndex-1, GrowDirection.grow_back) + valuesMap[index][charIndex] + fetchInt(index, charIndex+1, GrowDirection.grow_forward)
    return ''
def readDigitsFromIndex(index, charIndex):
    allValues.append(fetchInt(index-1, charIndex-1, GrowDirection.grow_both))
    allValues.append(fetchInt(index-1, charIndex+1, GrowDirection.grow_both))
    allValues.append(fetchInt(index-1, charIndex, GrowDirection.grow_both))
    
    allValues.append(fetchInt(index, charIndex-1, GrowDirection.grow_both))
    allValues.append(fetchInt(index, charIndex+1, GrowDirection.grow_both))


    allValues.append(fetchInt(index+1, charIndex-1, GrowDirection.grow_both))
    allValues.append(fetchInt(index+1, charIndex+1, GrowDirection.grow_both))
    allValues.append(fetchInt(index+1, charIndex, GrowDirection.grow_both))
def gearRatioFromIndex(index, charIndex):
    gearRatioValues = []
    gearRatioValues.append(fetchInt(index-1, charIndex-1, GrowDirection.grow_both))
    gearRatioValues.append(fetchInt(index-1, charIndex+1, GrowDirection.grow_both))
    gearRatioValues.append(fetchInt(index-1, charIndex, GrowDirection.grow_both))
    
    gearRatioValues.append(fetchInt(index, charIndex-1, GrowDirection.grow_both))
    gearRatioValues.append(fetchInt(index, charIndex+1, GrowDirection.grow_both))


    gearRatioValues.append(fetchInt(index+1, charIndex-1, GrowDirection.grow_both))
    gearRatioValues.append(fetchInt(index+1, charIndex+1, GrowDirection.grow_both))
    gearRatioValues.append(fetchInt(index+1, charIndex, GrowDirection.grow_both))    

    gearRatioTotal = 1
    gearRatioCount = 0
    for val in gearRatioValues:
        if val.isdigit():
            gearRatioTotal *= int(val)
            gearRatioCount += 1
    if gearRatioCount  == 2:
        return gearRatioTotal
    return 0
def reset_to_0(arr):
    for i, e in enumerate(arr):
        if isinstance(e, list):
            reset_to_0(e)
        else:
            arr[i] = 0
#----------------------

#Part 1 iterate through each value in valuesMap array
for index, line in enumerate(valuesMap):
    for charIndex, char in enumerate(line):
        if isSpecialCharacter(char):
            readDigitsFromIndex(index, charIndex)
#sum
sum = 0 
for value in allValues:
    if value.isdigit():
        sum += int(value)
print(sum)
#Part 2: iterate through and get gear ratios only 
allValues = []
reset_to_0(valuesMask)
for index, line in enumerate(valuesMap):
    for charIndex, char in enumerate(line):
        if (char) == '*':
            allValues.append(int(gearRatioFromIndex(index, charIndex)))
# sum all values in allValues
sum = 0
for value in allValues:
    sum += value
print((sum))