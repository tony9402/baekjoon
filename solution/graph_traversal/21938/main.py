# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/90c6fd1227d343279e7b9242cca023e3

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    q = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] >= t and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 1


n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    avg = []
    for i in range(0, m*3, 3):
        avg.append(int(sum(tmp[i:i+3])/3))
    graph.append(avg)
t = int(input())

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] >= t and not visited[i][j]:
            cnt += bfs(i, j)

print(cnt)
