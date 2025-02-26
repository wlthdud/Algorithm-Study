import sys
import queue
from collections import deque

input = sys.stdin.readline
N = int(input())

card_queue = deque(range(1,N+1))

for _ in range(N):
    if len(card_queue) != 1:
        card_queue.popleft()
        first = card_queue.popleft()
        card_queue.append(first)

print(card_queue[0])