N = int(input())
total = 0

for i in range(1, N):
    a=list(map(int,str(i)))
    s=i+sum(a)
    if s==N:
        total=i
        break

print(total)
