with open("2_1_input.txt", 'r') as file:
    tokens = file.readline().split(',')

token_tuples = []
for token in tokens:
    token_tuples.append(tuple(token.split("-")))

print(token_tuples)

def is_invalid(num):
    n = len(str(num))
    for i in range(1,n//2 + 1):
        if str(num)[0:i] * (n // i) == str(num):
            return True


invalid_sum = 0
for token in token_tuples:
    lower = int(token[0])
    upper = int(token[1])
    for i in range(lower, upper + 1):
        if is_invalid(i):
            invalid_sum += i

print(invalid_sum)