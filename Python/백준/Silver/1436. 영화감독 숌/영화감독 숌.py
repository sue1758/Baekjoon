N = int(input())
num = 666
on = 1

while True:
    if '666' in str(num):
        if on==N:
            break
        on+=1
    num+=1

print(num)