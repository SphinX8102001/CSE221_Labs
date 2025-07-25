import sys
a,b = map(int,sys.stdin.readline().split())
result = 1            
while b > 0:
    if b % 2 == 1:
        result = ( result * a ) % 107
    a = (a * a) % 107
    b = b // 2   
print(result)              