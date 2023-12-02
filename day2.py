import re
filename = "day2.txt"

with open(filename, "r") as file:
    lines = []
    for line in file:
        # Process each line here
        lines.append(line.strip())  # Example: Print each line after stripping whitespace
pattern = r"Game (\d+): (.+)"
totalGameSum = 0
totalGameGoal = {
    "red": 12,
    "green": 13,
    "blue": 14
}
for line in lines:
    match = re.match(pattern, line)
    if match:
        minCubes = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
        game_number = match.group(1)
        game_hands = match.group(2)
        totalGames = game_hands.split(';')
        fairGame = True
        for game in totalGames:
            for hand in game.strip().split(', '):
                print (hand)
                print (hand.split(' '))
                num = int(hand.split(' ')[0])
                color = hand.split(' ')[1]
                if num > minCubes[color]:
                    minCubes[color] = num
        totalCubeValue = minCubes["red"] * minCubes["green"] * minCubes["blue"]
        totalGameSum += int(totalCubeValue)
print(totalGameSum)
#        print(f"Game Number: {game_number}")
#        print(f"Game Hands: {game_hands}")
# for line in lines:
#     lineParse = line.split(':')
#     gameNumber = lineParse[0].split(' ')[1]
#     gameHands = lineParse[1].split(';')
#     print(game)
#     break




