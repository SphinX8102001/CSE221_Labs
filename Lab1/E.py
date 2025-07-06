def can_sort_with_reversals(n, arr):
    if n <= 2:
        return True
    working_arr = arr.copy()
    sorted_arr = sorted(arr)
    
    made_change = True
    while made_change:
        made_change = False
        for i in range(n - 2):  
            
            sub_arr = working_arr[i:i+3]
            reversed_sub = sub_arr[::-1]
            correct_before = sum(1 for j in range(n) if working_arr[j] == sorted_arr[j])
            
            temp_arr = working_arr.copy()
            temp_arr[i:i+3] = reversed_sub
            correct_after = sum(1 for j in range(n) if temp_arr[j] == sorted_arr[j])
            if correct_after > correct_before:
                working_arr[i:i+3] = reversed_sub
                made_change = True
                if working_arr == sorted_arr:
                    return True
    
    return working_arr == sorted_arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if can_sort_with_reversals(n, arr):
        print("YES")
    else:
        print("NO")

main()