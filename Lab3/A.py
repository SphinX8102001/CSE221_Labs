import sys 
inversion_count = 0
def merge(a,b):
    global inversion_count
    k = (len(a+b)//2) + 1
    arr = []
    i,j = 0,0
    while len(a) > i and len(b) > j:
        if a[i] <= b[j]:
            arr.append(a[i])
            i+=1
        elif a[i] > b[j]:
            arr.append(b[j])
            inversion_count += len(a) - i
            j+=1
    arr.extend(a[i:])
    arr.extend(b[j:])
    return arr
def merge_sort(a):
    mid = len(a)//2
    if len(a) == 1:
        return a
    else:
        a1 = merge_sort(a[:mid])
        a2 = merge_sort(a[mid:])
        return merge(a1,a2)
n = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip().split()
arr = [int(x) for x in arr]
srted_arr = merge_sort(arr)
print(inversion_count)
for i in range(n):
    if i == n-1:
        print(srted_arr[i])
    else:
        print(srted_arr[i], end = " ")


