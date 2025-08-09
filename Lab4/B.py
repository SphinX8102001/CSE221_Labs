def AdjListTOMatrix():
    N, M = map(int, input().split())
    u_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))
    w_l = list(map(int, input().split()))

    new_list = [[] for _ in range(N)]

    for i in range(M):
        u = u_list[i]
        v = w_list[i]
        w = w_l[i]
        new_list[u - 1].append((v, w))

    for k in range(N):
        print(f"{k + 1}:", end=" ")
        for neighbor, weight in new_list[k]:
            print(f"({neighbor},{weight})", end=" ")
        print()

AdjListTOMatrix()