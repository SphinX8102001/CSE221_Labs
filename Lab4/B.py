#B

def matrix():
    N, M = map(int, input().split())
    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))

    new_list = [[] for _ in range(N)]

    for i in range(M):
        u = u_list[i]
        v = v_list[i]
        w = w_list[i]
        new_list[u - 1].append((v, w))

    for k in range(N):
        print(f"{k + 1}:", end=" ")
        for neighbor, weight in new_list[k]:
            print(f"({neighbor},{weight})", end=" ")
        print()

matrix()