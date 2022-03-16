# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/f54caa5c821440d596a604a6df4e8d68

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
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 직사각형 채우기
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if not graph[x][y]:
                graph[x][y] = 1

# 빈 영역 탐색하기
ans = []
for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            ans.append(bfs(i, j))
ans.sort()

print(len(ans), ' '.join(map(str, ans)), sep='\n')
