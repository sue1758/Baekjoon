while 1:
    n=int(input())
    if n==-1:
        break
    list=[]
    for i in range(1,n):
        if n%i==0:
            list.append(i)

    if sum(list)==n:
        temp=" + ".join(str(i) for i in list)
        print(f"{n} = {temp }")
    else:
        print(f"{n} is NOT perfect.")
