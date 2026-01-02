A=[]

for i in range(5):
    A.append(input())

result=''

for j in range(15):
    for i in range(5):
        if j<len(A[i]):
            print(A[i][j], end='')