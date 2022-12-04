def read_file(filename):
    with open(filename,"r", encoding="utf-8") as file:
        lines = file.readlines() 
        lines = list(map(lambda x:x.strip(), lines)) 
    return lines 

# print(read_file("day_1_test.txt"))


lines = read_file("day_1_2022.txt")

elves = [[]]


for calories in lines:

    if calories == "":
        elves.append([])
    else:
        elves[len(elves)-1].append(int(calories))
    
totals = []
for elf in elves: 
    totals.append(sum(elf))



print(max(totals))
