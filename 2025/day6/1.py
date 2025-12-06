with open ("2025/day6/input.txt") as f:
    lines = [list(line.rstrip("\n").split()) for line in f.readlines()]

total = 0
for i in range(len(lines[0])):
    match lines[-1][i]:
        case "+":
            sum = 0
            for j in range(len(lines)-1):
                sum += int(lines[j][i])
        case "*":
            sum = 1
            for j in range(len(lines)-1):
                sum *= int(lines[j][i])
    total += sum

print(total)