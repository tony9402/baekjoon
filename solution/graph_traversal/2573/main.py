# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/04adde851be5406c89d8a705f4594295

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    sea += 1
                elif visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            ice.append((i, j))

year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] > 0 and visited[i][j] == 0:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = list(set(ice) - set(delList))
    year += 1

if group < 2:
    print(0)
