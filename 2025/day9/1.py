with open ("2025/day9/input.txt") as f:
    lines = f.read().splitlines()
    tuples = []
    for line in lines:
        tuples.append(tuple(int(x) for x in line.split(",")))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def dist_to_UL(a):
    return dist(a, (0,0))
def dist_to_UR(a):
    return dist(a, (max_x,0))
def dist_to_DL(a):
    return dist(a, (0,max_y))
def dist_to_DR(a):
    return dist(a, (max_x,max_y))

def area(a, b):
    len1 = abs(a[0] - b[0]) + 1
    len2 = abs(a[1] - b[1]) + 1
    return len1 * len2

UL = tuples[0]
UR = tuples[0]
DL = tuples[0]
DR = tuples[0]
g = [UL, UR, DL, DR]

max_x = -1
max_y = -1

for node in tuples:
    if node[0] > max_x:
        max_x = node[0]
    if node[1] > max_y:
        max_y = node[1]

for node in tuples:
    if dist_to_UL(node) < dist_to_UL(g[0]):
        g[0] = node
    if dist_to_UR(node) < dist_to_UR(g[1]):
        g[1] = node
    if dist_to_DL(node) < dist_to_DL(g[2]):
        g[2] = node
    if dist_to_DR(node) < dist_to_DR(g[3]):
        g[3] = node

max = -1
for outer in g:
    for inner in g:
        if area(outer, inner) > max:
            max = area(outer, inner)
print(max)