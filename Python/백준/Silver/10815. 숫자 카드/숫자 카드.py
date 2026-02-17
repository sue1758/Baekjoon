N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_count = {}
for n in N_list:
    N_count[n] = True

for m in M_list:
    if m in N_count:
        print(1, end = ' ')
    else:
        print(0, end = ' ')