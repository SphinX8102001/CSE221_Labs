import sys

def can_be_sorted(arr):
    n = len(arr)
    for _ in range(n * n):
        changed = False
        for i in range(n - 2):
            if arr[i] > arr[i+1] or arr[i+1] > arr[i+2] or arr[i] > arr[i+2]:
                arr[i:i+3] = reversed(arr[i:i+3])
                changed = True
        if not changed:
            break 
    
    return arr == sorted(arr)


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

if N <= 2:
    print("YES")
else:
    print("YES" if can_be_sorted(arr) else "NO")
