#Authored by : gkgg123
#Co-authored by : -
#Link : https://www.acmicpc.net/source/share/061583cd645e449d9936ecd6491016f4
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<M):continue
            if visited[nx][ny] or not field[x][y]:continue
            queue.append((nx,ny))
            visited[nx][ny] = True

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int,input().split())
        field[x][y] = 1
    result = 0
    for x in range(N):
        for y in range(M):
            if field[x][y] and not visited[x][y]:
                bfs(x,y)
                result += 1

    print(result)
