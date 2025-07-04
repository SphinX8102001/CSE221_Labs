import sys

no_of_elements = int(sys.stdin.readline())

arr = sys.stdin.readline().strip().split(" ")
arr = [int(_) for _ in arr]
for j in range(no_of_elements):
    for i in range(1,no_of_elements):
        n1 = arr[i-1]
        n2 = arr[i]
        is_n1_even = False
        is_n2_even = False

        if n1 % 2 == 0:
            is_n1_even = True
        if n2 % 2 == 0:
            is_n2_even = True
        if is_n1_even == is_n2_even :
            if n1 > n2:
                arr[i-1],arr[i] =arr[i],arr[i-1]

for _ in range(no_of_elements):
    if _ == no_of_elements - 1:
        print(arr[_])
    else:
        print(arr[_], end=" ")