with open ("2025/day4/input.txt") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))
lines = ["." + line + "." for line in lines]
for i, line in enumerate(lines):
    lines[i] = list(line)

accessible = 0
to_remove = []
while True:
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == ".":
                continue
            paper_count = -1
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if lines[i + l][j + k] == "@":
                        paper_count += 1
            if paper_count < 4:
                accessible += 1
                to_remove.append((i, j))
    if not to_remove:
        break
    for i, j in to_remove:
        lines[i][j] = "."
    to_remove = []
print(accessible)
