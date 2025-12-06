with open ("2025/day6/input.txt") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]
split_indexes = []
for i in range(len(lines[0].rstrip("\n"))):
    if lines[-1][i] in ("+", "*"):
        split_indexes.append(i)
split_indexes.pop(0)

new_lines = []
for i in range(len(lines)):
    new_line = []
    last_index = 0
    for index in split_indexes:
        new_line.append(lines[i][last_index:index-1])
        last_index = index
    new_line.append(lines[i][last_index:])
    new_lines.append(new_line)

total = 0
for i in range(len(new_lines[0])):
    match new_lines[-1][i][0]:
        case "+":
            sum = 0
            for j in range(len(new_lines[0][i])):
                num = ""
                for k in range(len(new_lines)-1):
                    num += str(new_lines[k][i][j-1])
                sum += int(num)
        case "*":
            sum = 1
            for j in range(len(new_lines[0][i])):
                num = ""
                for k in range(len(new_lines)-1):
                    num += str(new_lines[k][i][j-1])
                sum *= int(num)
    total += sum

print(total)
