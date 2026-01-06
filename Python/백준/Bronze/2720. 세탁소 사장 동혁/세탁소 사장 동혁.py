co = int(input())
for _ in range(co):
    c = int(input())

    for i in [25, 10, 5, 1]:
        print(c // i, end=" ")
        c %= i