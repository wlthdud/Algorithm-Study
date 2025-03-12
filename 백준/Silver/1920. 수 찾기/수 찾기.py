from sys import stdin
N = int(stdin.readline())
N_set = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

for i in M_list:
    if i in N_set:
        print(1)
    else:  
        print(0)