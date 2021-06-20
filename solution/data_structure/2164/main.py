# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/a8466e811f55412d993474fd417f4631
import sys
from collections import deque

queue = deque()
N = int(input())
for i in range(1,N+1):
    queue.append(i)

while True:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)