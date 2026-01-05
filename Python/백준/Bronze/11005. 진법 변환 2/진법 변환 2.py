string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n,b=map(int, input().split())
ans=''

while n!=0:
    ans+=string[n%b]
    n//=b

print(ans[::-1])