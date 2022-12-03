
scoreDict = {
    "rock":1,
    "paper":2,
    "scissors":3
}

winners  = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
    
}

fights = []
score = 0

with open('./rockPaperScissors.txt', 'r') as file:
    for line in file:
        tmp = line.strip().split(" ")
        for i, x in enumerate(tmp):
            if x == "A" or x == "X":
                tmp[i] = "rock"
            elif x == "B" or x == "Y":
                tmp[i] = "paper"
            else:
                tmp[i] = "scissors"
        fights.append(tmp)
for fight in fights:
    if fight[0] == fight[1]:
        score += (3 + scoreDict[fight[1]])
    elif fight[0] == winners[fight[1]]:
        score += (6 + scoreDict[fight[1]])
    else:
        score += scoreDict[fight[1]]

print(score)