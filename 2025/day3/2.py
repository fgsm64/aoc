with open ("input.txt") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

total = 0
for line in lines:
    stack = []
    droppable = len(line) - 12
    for char in line:
        while stack and int(stack[-1]) < int(char) and droppable > 0:
            stack.pop()
            droppable -= 1
        stack.append(char)

    while len(stack) > 12:
        stack.pop()

    total += int("".join(stack))

print(total)
