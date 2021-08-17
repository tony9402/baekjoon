# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/056db524c16f458c9bc7a5beb2c35da8

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(x,y):
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = 1
    while queue:
        q = queue.popleft()
        for i in range(4):
            dx = nx[i] + q[0]
            dy = ny[i] + q[1]
            if dx < 0 or dx >= L or dy < 0 or dy >= W:
                continue
            if visited[dx][dy] == 0 and arr[dx][dy] == 'L':
                visited[dx][dy] = 1
                queue.append((dx,dy,q[2]+1))
    return q[2]

L, W = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
MIN_CT = 0

for i in range(L):
    arr.append(input())

for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L':
            visited = [[0 for i in range(W)] for j in range(L)]
            ct = BFS(i,j)
            MIN_CT = max(MIN_CT, ct)
print(MIN_CT)
