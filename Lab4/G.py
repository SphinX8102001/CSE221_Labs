def main():
    N, M, K = map(int, input().split())
    position = []
    for _ in range(K):
        x, y = map(int, input().split())
        position.append((x, y))

    a_set = set(position)
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    flag = False
    for i, j in position:
        for k, l in moves:
            atk_x = i + k
            atk_y = j + l
            if 1 <= atk_x <= N and 1 <= atk_y <= M:
                if (atk_x, atk_y) in a_set:
                    print("YES")
                    flag = True
                    break
        if flag:
            break

    if not flag:
        print("NO")

main()        