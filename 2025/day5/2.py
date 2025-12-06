with open ("2025/day5/input.txt") as f:
    lines = f.readlines()
    ranges = []
    for i, line in enumerate(lines):
        if line == "\n":
            break
        a, b = line.rstrip("\n").split("-")
        ranges.append((int(a), int(b)))


ranges.sort()
merged = []
for start, end in ranges:
    if not merged:
        merged.append([start, end])
        continue
    last_start, last_end = merged[-1]
    if start <= last_end + 1:
        if end > last_end:
            merged[-1][1] = end
    else:
        merged.append([start, end])

count = 0
for start, end in merged:
    count += end - start + 1

print(count)
