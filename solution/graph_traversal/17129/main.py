# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/f037e6fe919b49d09b31c05df27614c8

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(time, x, y):
    q = deque([(time, x, y)])
    visited[x][y] = 1
    while q:
        time, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1 and not visited[nx][ny]:
                if graph[nx][ny] > 2:
                    print('TAK')
                    print(time + 1)
                    return 1
                q.append((time + 1, nx, ny))
                visited[nx][ny] = 1
    print('NIE')

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))
    if 2 in graph[i]:
        x, y = i, graph[i].index(2) # 출발지점인 식구의 좌표를 x, y에 저장

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, x, y)
