# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/1cf1ea352dba44daa9768b67c7f109e9
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)