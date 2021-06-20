# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/6bf4491116ff480fab750a65591c134e

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

queue = deque()
N = int(input())
for i in range(N):
    com = input().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif com[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)