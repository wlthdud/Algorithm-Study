n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

num_set = set(num_list)
result = 0

for i in num_list:
    if x-i in num_set:
        result += 1

    
print(result//2)