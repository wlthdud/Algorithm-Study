arr = []

for _ in range(9):
    num = int(input())
    arr.append(num)

exceed_num = sum(arr) - 100

for i in range(8):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == exceed_num :
            del arr[j]
            del arr[i]
            break
    if len(arr) == 7: 
        break
    
for j in arr:
    print(j)