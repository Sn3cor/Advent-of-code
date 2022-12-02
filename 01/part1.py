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

    maxCal = max(elves)
    print(maxCal)