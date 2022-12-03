groupItemTypes =[]
priorities = []
lines = []
groupedStrings = []
lowercaseAsciiShift = 96
uppercaseAsciiShift = 38
with open('./input.txt','r') as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        if (lines.index(line) + 1) % 3 != 0:
            groupedStrings.append(line)
        else:
            groupedStrings.append(line)
            for string in groupedStrings:
                for char in string:
                    if char in groupedStrings[1]:
                        if char in groupedStrings[2]:
                            groupItemTypes.append(char)
                            break;
                break
            groupedStrings.clear()

            
for el in sorted(groupItemTypes):
    if el == el.upper():
        priorities.append(ord(el) - uppercaseAsciiShift)
    else:
        priorities.append(ord(el) - lowercaseAsciiShift)

print(sum(priorities))
