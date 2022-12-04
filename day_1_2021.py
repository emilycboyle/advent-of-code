def read_file(filename):
    with open(filename,"r", encoding="utf-8") as file:
        lines = file.readlines() 
        lines = list(map(lambda x:x.strip(), lines)) 
    return lines 

# print(read_file("day_1_test.txt"))


lines = read_file("day_1.txt")
lines = list(map(int, lines))
index = 1
count = 0
while index < len(lines):
    increase = lines[index] > lines[index-1]
    if increase:
        count +=1
    # print(lines[index])
    # print(increase)
    index +=1

print(count)
