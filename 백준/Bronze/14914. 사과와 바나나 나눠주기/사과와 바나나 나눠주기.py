a, b = map(int, input().split())

def find_divisors(x, y):
    gcd_divisors = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd_divisors.append(i)
    return gcd_divisors

common_divisors = find_divisors(a, b)

for k in common_divisors:
    print(k, a // k, b // k)
