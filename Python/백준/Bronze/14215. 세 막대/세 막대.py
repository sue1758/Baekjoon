a,b,c=map(int, input().split())

max= max(a,b,c)
mid= a+b+c-max

if max<mid:
    print(a+b+c)
else:
    max=mid-1
    print(mid+max)
