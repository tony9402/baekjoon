# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/1be97bce103a4572936b311c3f1a096b

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(x,y):
    global flag, total
    queue = deque()
    queue.append((x,y))
    ans.append((x,y))
    while queue:
        q = queue.popleft()
        for i in range(4):
            dx = nx[i] + q[0]
            dy = ny[i] + q[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            if visited[dx][dy] == 1:
                continue
            if abs(arr[dx][dy] - arr[q[0]][q[1]]) >= L and abs(arr[dx][dy] - arr[q[0]][q[1]]) <= R:
                visited[dx][dy] = 1
                flag = 1
                total += arr[dx][dy]
                queue.append((dx,dy))
                ans.append((dx,dy))

N, L, R = map(int, input().split())
arr = []
day = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
for i in range(N):
    arr.append(list(map(int, input().split())))
while True:
    flag = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                ans = deque()
                total = arr[i][j]
                visited[i][j] = 1
                BFS(i,j)
                if len(ans) > 1:
                    aver = total // len(ans)
                    while ans:
                        a = ans.popleft()
                        arr[a[0]][a[1]] = aver
    if not flag:
        break
    day += 1
print(day)