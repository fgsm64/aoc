with open ("2025/day5/input.txt") as f:
    lines = f.readlines()
    ranges = []
    ids = []
    for i, line in enumerate(lines):
        if line == "\n":
            seperator_index = i
            break
        a, b = line.rstrip("\n").split("-")
        ranges.append((int(a), int(b)))
    for i in range(seperator_index+1, len(lines)):
        ids.append(lines[i].rstrip("\n"))

for i, id in enumerate(ids):
    ids[i] = int(id)

valid_count = 0
for id in ids:
    for start, end in ranges:
        if start <= id <= end:
            valid_count += 1
            break

print(valid_count)