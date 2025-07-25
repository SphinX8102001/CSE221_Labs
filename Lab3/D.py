import sys
def mult_matrix(mat1, mat2):
    mod = 10**9 + 7
    result =[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + mat1[i][k] * mat2[k][j]) % mod
    return result

def mat_pow(mat, x):
    if x == 0:
        return [[1,0],[0,1]]
    if x % 2 == 0:
        half_pow = mat_pow(mat,x //2)
        return mult_matrix(half_pow,half_pow)
    else:
        return mult_matrix(mat_pow(mat,x-1), mat)

T = int(sys.stdin.readline())
for _ in range(T):
    x11,x12,x21,x22 = map(int, sys.stdin.readline().split())
    A = [[x11,x12],[x21,x22]]
    X = int(sys.stdin.readline())
    result = mat_pow(A,X)
    print(result[0][0], result[0][1])            
    print(result[1][0], result[1][1])