# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/102afab5148c43ad8c8d179d80117e24
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(x):

    queue = deque()
    queue.append((x,1))

    while queue:
        q = queue.popleft()
        if q[0] == B:
            return q[1]

        if q[0] * 10 + 1 <= B:
            queue.append((q[0] * 10 + 1, q[1]+1))

        if q[0] * 2 <= B:
            queue.append((q[0] * 2, q[1]+1))

    return -1

A, B = map(int, input().split())
ans = BFS(A)
print(ans)