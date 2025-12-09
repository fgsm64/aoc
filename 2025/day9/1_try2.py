with open ("2025/day9/input.txt") as f:
    lines = f.read().splitlines()
    tuples = []
    for line in lines:
        tuples.append(tuple(int(x) for x in line.split(",")))

max_area = 0
for i in range(len(tuples)):
    for j in range(i+1, len(tuples)):
        width = abs(tuples[i][0] - tuples[j][0]) + 1
        height = abs(tuples[i][1] - tuples[j][1]) + 1
        if (width * height) > max_area:
            max_area = width * height
print(max_area)