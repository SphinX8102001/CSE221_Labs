import sys

num_of_tests = int(sys.stdin.readline())
def checker():
    if flag:
        print("NO")
    else:
        print("YES")

for _ in range(num_of_tests):
    num_of_elements_in_the_arr = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().split())
    arr = [int(_) for _ in arr]
    flag = False
    if num_of_elements_in_the_arr == 1:
        print("YES")
        continue
    else:
        for i in range(1, num_of_elements_in_the_arr):
            if arr[i] < arr[i - 1]:
                flag = True
                break
    checker()
