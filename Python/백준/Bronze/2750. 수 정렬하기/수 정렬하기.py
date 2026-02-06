N=int(input())
lists=[]

for i in range(N):
    lists.append(int(input()))

lists2=sorted(lists)
    
for i in range(len(lists)):
    print(lists2[i])
