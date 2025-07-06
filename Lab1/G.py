def count_swaps_and_sort(n, ids, marks):
    students = [(marks[i], ids[i], i) for i in range(n)]
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            curr = students[j]
            next = students[j+1]
            if (curr[0] < next[0]) or (curr[0] == next[0] and curr[1] > next[1]):
                students[j], students[j+1] = students[j+1], students[j]
                swaps += 1
    
    return swaps, students

def main():
    
    n = int(input())
    ids = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    swaps, sorted_students = count_swaps_and_sort(n, ids, marks)
    print(f"Minimum swaps: {swaps}")
    for mark, id, _ in sorted_students:
        print(f"ID: {id} Mark: {mark}")

main()

