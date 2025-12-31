hangs=[]
yuls=[]

for i in range(9):
  a = list(map(int,input().split()))
  hangmax = max(a)
  yulmax = a.index(hangmax) +1
  hangs.append(hangmax)
  yuls.append(yulmax)

print(max(hangs))
loc = hangs.index(max(hangs))
print((loc+1), yuls[loc])
