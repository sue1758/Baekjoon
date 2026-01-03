n=int(input())

papers=[]

for _ in range(n):
    papers.append(list(map(int,input().split())))

area = 0

for i in range(100):
    for j in range(100):
        for x,y in papers:
            if x<=i<x+10 and y<=j<y+10:
                area+=1
                break
print(area)
