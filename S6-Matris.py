import random

def matrix(a,b):
    mat = [[random.randint(0,10) for i in range(a)]for j in range(b)]
    return mat

k = int(input('Enter K :'))
n = int(input('Enter N :'))
m = int(input('Enter M :'))

Matrix1 = matrix(m,n)
Matrix2 = matrix(k,m)
Matrix3=[[0 for i in range(k)]for j in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            Matrix3[i][j]+=(Matrix1[i][z]*Matrix2[z][j])        
        
print(Matrix3)
