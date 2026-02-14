n = int(input())
alpha = [str(input()) for i in range(n)]

alpha = list(set(alpha))
alpha.sort()
alpha.sort(key=len)

for i in alpha:
    print(i)
