with open('./calories.txt', "r") as file:
    elves = []
    elf = []
    
    for line in file:
        line = line.replace('\n',"")
        if line:
            elf.append(int(line))
        else:
            elves.append(sum(elf))
            elf.clear()
            
    descElves = elves.sort(reverse=True)
    topThreeSum = sum(elves[0:3])
    print(topThreeSum)
