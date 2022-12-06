
def read_file(filename):
    with open(filename,"r", encoding="utf-8") as file:
        lines = file.readlines() 
    return lines 
lines = read_file("day_3_test.txt")

line = list(lines[0].strip())
index = int(len(line)/2)
first_half = line[0:index]

last_half = line[index:len(line)]

set_1, set_2 = set(first_half), set(last_half)

commoners = set_1.intersection(set_2)
print(commoners)


