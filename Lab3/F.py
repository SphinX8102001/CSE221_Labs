import sys
n = int(sys.stdin.readline())
a = list(map(int, input().split()))

final = []

def new_order(arr,low,high):
    if low > high:
        return
    mid = (low+high)//2
    final.append(arr[mid])
    new_order(arr,low,mid-1)
    new_order(arr,mid + 1,high)
new_order(a,0,n-1)
print(*final)

