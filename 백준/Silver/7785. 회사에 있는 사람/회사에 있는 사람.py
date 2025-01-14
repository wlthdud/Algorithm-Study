n = int(input())
enter_set = set()

for i in range(n):
    log = input().split()
    name, status = log[0], log[1]
    if status == 'enter':
        enter_set.add(name)
    elif status == 'leave':
        enter_set.discard(name)
        
enter_list = sorted(enter_set, reverse=True)

for name in enter_list:
    print(name)