from sys import stdin
from collections import Counter

N = int(stdin.readline())
num_list = []

for i in range(N):
    num_list.append(int(stdin.readline()))
    
num_list.sort()

#산술평균
print(round(sum(num_list)/N))

#중앙값
print(num_list[round(N//2)])

#최빈값
count = Counter(num_list).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

#범위
print(max(num_list) - min(num_list))
