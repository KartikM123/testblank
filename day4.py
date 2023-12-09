import re
filename = "day4.txt"

with open(filename, "r") as file:
    lines = []
    pattern = r"(\w+)\|(\w+)"
    for line in file:
        match = line.split(":")[1]
        #print(line.split(":")[1])
        #print(line.strip())
        if match:
            #card_number = match.group(1)
            hand1 = match.split("|")[0]
            hand2 = match.split("|")[1]
            # Process the extracted values here
            lines.append((hand1.split(" "), hand2.split(" ")))
print(lines[0])
# part 1
total = 0
for val in lines:
    winCount = -1
    for wins in val[0]:
        if wins.isdigit():
            for set in val[1]:
                if wins == set.strip():
                    winCount += 1
    if (winCount > -1):
        total += pow(2, winCount)
# part 2
total = 0
ind = 0
arrStackIndex = []
for i in range(0, len(lines)):
    arrStackIndex.append(1)
while ind < len(lines):
    print (arrStackIndex)
    val = lines[ind]
    winCount = 0
    total += arrStackIndex[ind]
    #count wins for card
    for wins in val[0]:
        if wins.isdigit():
            for set in val[1]:
                if wins == set.strip():
                    winCount += 1
    #based on wins for card then move out
    while winCount > 0:
        if ind + winCount < len(lines):
            arrStackIndex[ind + winCount] += arrStackIndex[ind]
        winCount -= 1
    #stop stacking at this index
    arrStackIndex[ind] = 0
    if arrStackIndex[ind] == 0:
        ind += 1
print(total)