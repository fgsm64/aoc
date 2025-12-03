with open ("input.txt") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

total = 0
for line in lines:
    max = -1
    max_index = -1
    second_max = -1
    line_string = str(line)
    for i, char in enumerate(line_string):
        if int(char) > max:
            max = int(char)
            max_index = i
    if max_index == len(line_string) - 1:
        new_string = line_string[:max_index]
        last = True
    else:
        new_string = line_string[max_index+1:]
        last = False
    for i, char in enumerate(new_string):
        if int(char) > second_max:
            second_max = int(char)
    if last:
        total += int(str(second_max)+str(max))
    else:
        total += int(str(max)+str(second_max))

print(total)
