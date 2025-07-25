import bisect
def countinversion():
    n=int(input())
    Arr=list(map(int, input().split()))
    ct=0
    final=[]
    for i in Arr:
        sq=i*i
        ind=bisect.bisect_right(final, sq)
        ct+=len(final)-ind
        bisect.insort(final, i)
    print(ct)
countinversion()