def main():
    N = int(input())
    x, y = map(int, input().split())

    l = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            l_1, l_2 = x + i, y + j
            if 1 <= l_1 <= N and 1 <= l_2 <= N:
                l.append((l_1, l_2))

    print(len(l))
    for move in sorted(l):
        print(move[0], move[1])

main()