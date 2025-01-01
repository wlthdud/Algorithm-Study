N, M = map(int, (input().split()))
arr = list(map(int, input().split()))

arr_sum = 0
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:    
                arr_sum = arr[i]+arr[j]+arr[k]
                if result <= arr_sum:
                    result = arr_sum
                
print(result)