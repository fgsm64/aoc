with open("1_1_input.txt", 'r') as file:
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
            initial -= token[1]
        case "R":
            initial += token[1]
    initial = initial % 100
    if initial == 0:
        zero_count += 1

print(zero_count)
        

