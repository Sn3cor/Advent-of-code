itemTypes =[]
priorities = []
lowercaseAsciiShift = 96
uppercaseAsciiShift = 38
with open('./input.txt','r') as file:
    for line in file:
        line = line.strip()
        leftHalf = line[:int(len(line)/2)]
        rightHalf = line[int(len(line)/2):]
        for char in leftHalf:
            if char in rightHalf:
                itemTypes.append(char)
                break;


for el in sorted(itemTypes):
    if el == el.upper():
        priorities.append(ord(el) - uppercaseAsciiShift)
    else:
        priorities.append(ord(el) - lowercaseAsciiShift)

print(sum(priorities))
