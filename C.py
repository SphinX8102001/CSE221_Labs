import sys 

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    math = n * (n+1) / 2
    print(int(math))

