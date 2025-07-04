T = int(input())
for i in range(T):
    user_input = input()
    token = user_input.split()
    if token[2] == '+':
        output = int(token[1]) + int(token[3])
    elif token[2] == '-':
        output = int(token[1]) - int(token[3])
    elif token[2] == '*':
        output = int(token[1]) * int(token[3])
    elif token[2] == '/':
        output = int(token[1]) / int(token[3])
    print(output)
