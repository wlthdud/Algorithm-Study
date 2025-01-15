N,M = map(int, input().split())
N_list = []
M_list = []

for i in range(N):
    N_list.append(input())
    
for i in range(M):
    M_list.append(input())

result = sorted(list(set(N_list) & set(M_list)))

print(len(result))

for k in result:
    print(k)