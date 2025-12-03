with open("input.txt", 'r') as file:
    tokens = file.readlines()

tokens_trimmed_newline = [line.rstrip('\n') for line in tokens]
tokens_tuples = []
for line in tokens_trimmed_newline:
    tokens_tuples.append((line[0], int(line[1:])))

initial = 50
zero_count = 0
for token in tokens_tuples:
    match token[0]:
        case "L":
            previous = initial
            initial -= token[1]
            if initial <= 0:
                zero_count += (initial-1) // 100 * -1
                if previous == 0:
                    zero_count -= 1
        case "R":
            initial += token[1]
            if initial >= 100:
                zero_count += initial // 100
    initial = initial % 100

print(zero_count)
