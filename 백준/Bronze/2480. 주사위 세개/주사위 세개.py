from collections import Counter

dice_list = list(map(int, input().split()))
count_dice = Counter(dice_list)

if 3 in count_dice.values():
    num = [k for k, v in count_dice.items() if v == 3][0]
    print(10000 + num * 1000)
elif 2 in count_dice.values():
    num = [k for k, v in count_dice.items() if v == 2][0]
    print(1000 + num * 100)
else:
    print(max(dice_list) * 100)
