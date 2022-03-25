# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/1b8f001e0d3241ada8e1074f213f88d4

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

n, m, k = map(int, input().split())
graph = [['_'] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = '#'

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#' and not visited[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)
