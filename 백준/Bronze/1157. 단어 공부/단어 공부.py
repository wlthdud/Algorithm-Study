words = input().strip().upper()
words_list = list(words)
words_set = list(set(words_list))

count_list = []

for i in words_set:
        count = words_list.count(i)
        count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(words_set[count_list.index(max(count_list))])
