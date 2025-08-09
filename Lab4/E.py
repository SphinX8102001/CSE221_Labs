def main():
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    degree_1 = [0] * N
    degree_2 = [0] * N

    for i in range(M):
        E = a_list[i] - 1
        V = b_list[i] - 1
        degree_2[E] += 1
        degree_1[V] += 1

    output = [degree_1[i] - degree_2[i] for i in range(N)]

    print(*output)

main()