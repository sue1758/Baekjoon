N = int(input())
a = 0
b = 0
remain = 0

for a in range(N//5,-1,-1):
    remain=N-(5*a)

    if remain % 3 == 0:
        b=remain//3

        print(a+b)
        break

else:
    print(-1)