def read_file(filename):
    with open(filename,"r", encoding="utf-8") as file:
        lines = file.readlines() 
        lines = list(map(lambda x:x.strip(), lines)) 
    return lines 

# print(read_file("day_1_test.txt"))


lines = read_file("day_1.txt")

def get_calories_for_elves():
    elves = [[]]
    for calories in lines:

        if calories == "":
            elves.append([])
        else:
            elves[len(elves)-1].append(int(calories))
        
    totals = []
    for elf in elves: 
        totals.append(sum(elf))

    return totals


def part_1():
    totals = get_calories_for_elves()
    print(max(totals))

part_1()

def part_2():
    totals = get_calories_for_elves()
    # sort totals by desc values
    # select top 3 values 
    # sum the top 3 

    totals.sort(reverse=True)

    print(totals)
    print(sum(totals[0:3]))

part_2()


