with open ("2025/day7/input.txt") as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        lines[i] = list(line)

count = 0
for i in range(len(lines)-1):
    for j, char in enumerate(lines[i]):
        if char == "S":
            lines[i+1][j] = "|"
        if char == "|":
            if lines[i+1][j] in (".", "|"):
                lines[i+1][j] = "|"
            elif lines[i+1][j] == "^":
                count += 1
                if j not in (0, len(lines[0])-1):
                    lines[i+1][j-1] = "|"
                    lines[i+1][j+1] = "|"

for line in lines:
    print(line)
    print()

print(count)