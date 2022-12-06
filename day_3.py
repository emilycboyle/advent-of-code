
def read_file(filename):
    with open(filename,"r", encoding="utf-8") as file:
        lines = file.readlines() 
    return lines 
lines = read_file("day_3.txt")


def get_common_values(line):
    index = int(len(line)/2)
    first_half = line[0:index]

    last_half = line[index:len(line)]

    set_1, set_2 = set(first_half), set(last_half)

    commoners = set_1.intersection(set_2)
    return commoners

common_items = []

for line in lines:
    shared = get_common_values(list(line.strip()))
    common_items.append(shared.pop())
print(common_items)

lowercase_diff = 96
uppercase_diff = 38
lowercase_boundary = ord('a')

def get_priority(item):
    is_lowercase = ord(item)>=lowercase_boundary  
    if is_lowercase:
        return ord(item)-lowercase_diff
    else:
        return ord(item)-uppercase_diff

priorities = []

for item in common_items:
    priority = get_priority(item)
    priorities.append(priority)

print(sum(priorities))