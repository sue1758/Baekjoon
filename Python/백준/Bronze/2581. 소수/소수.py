M = int(input()) 
N = int(input())
list = []
for num in range(M, N+1):
    prime = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                prime += 1
                break
        if prime == 0:
            list.append(num)
if len(list) > 0:
    print(sum(list))
    print(min(list))
else:
    print(-1)