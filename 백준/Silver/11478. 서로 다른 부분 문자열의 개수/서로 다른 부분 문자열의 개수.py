S = input()
result = set()

for i in range(len(S)):
    for j in range(len(S)):
        result.add(S[j:j+i])

print(len(result))