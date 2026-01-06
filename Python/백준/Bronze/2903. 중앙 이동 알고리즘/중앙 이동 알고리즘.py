N = int(input())
S = [0,0]
 
for _ in range(N):
    for i in range(1,len(S)*2-1,2):
        S.insert(i,0)
 
sum = S.count(0)
 
print(sum*sum)
