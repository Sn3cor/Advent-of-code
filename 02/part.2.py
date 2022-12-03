scoreDict = {
    "rock":1,
    "paper":2,
    "scissors":3
}
resultDict = {
    "X":"loss",
    "Y":"draw",
    "Z":"win"
}

winners  = {
    "scissors":"rock",
    "rock":"paper",
    "paper":"scissors"
    
}

losers = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

fights = []
score = 0

with open('./rockPaperScissors.txt', 'r') as file:
    for line in file:
        tmp = line.strip().split(" ")
        if tmp[0] == "A":
            tmp = ["rock", resultDict[tmp[1]]]
        elif tmp[0] == "B":
            tmp = ["paper", resultDict[tmp[1]]]
        else:
            tmp = ["scissors", resultDict[tmp[1]]]
        fights.append(tmp)

print(fights)
for fight in fights:
    if fight[1] == "draw":
        score += (3 + scoreDict[fight[0]])
    elif fight[1] == "win":
        score += (6 + scoreDict[winners[fight[0]]])
    else:
        score += scoreDict[losers[fight[0]]]

print(score)