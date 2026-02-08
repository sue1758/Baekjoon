lists=[]

for i in range(5):
    lists.append(int(input()))

lists2=sorted(lists)

print(int(sum(lists2)/5))
print(lists2[2])
