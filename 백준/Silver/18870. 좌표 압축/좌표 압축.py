from sys import stdin

N = int(stdin.readline())
N_list = list(map(int, stdin.readline().split()))


N_set = set(N_list)
N_set_sort = sorted(N_set)
N_list_sort = list(N_set_sort)

dic = {}

for i in range(len(N_list_sort)):
    dic[N_list_sort[i]] = i
    
for i in N_list:
    print(dic[i], end=" ")