def main():
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    degrees = [0] * N

    for i in range(M):
        E = a_list[i]
        V = b_list[i]
        degrees[E - 1] += 1
        degrees[V - 1] += 1

    degree_count = 0
    for i in degrees:
        if i % 2 != 0:
            degree_count += 1

    if degree_count == 0 or degree_count == 2:
        print("YES")
    else:
        print("NO")
main()        