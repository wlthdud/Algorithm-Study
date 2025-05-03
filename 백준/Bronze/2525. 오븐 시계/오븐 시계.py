from sys import stdin

A, B = map(int, stdin.readline().split())
C = int(stdin.readline())

total_min = A * 60 + B + C

A = (total_min // 60) % 24
B = total_min % 60

print(A, B)