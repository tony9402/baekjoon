# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/e3ce24674f424d2b812182fa48eb21b2

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def check_four(x, y):
    q = deque([(x, y)])
    now = graph[x][y]
    pos = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4: # 색이 같은 뿌요가 4개 이상 모여있다면
        pos.sort(key=lambda x: (x[1], x[0])) # 좌표 정렬
        for i, j in pos:
            graph[i][j] = '_' # 터뜨리기
            bombList.append((i, j)) # 뿌요들을 한 칸씩 내려주기 위해 터뜨린 곳 좌표 저장

graph = [list(input()) for i in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    bombList = []
    
    # 뿌요 체크해서 터뜨리기
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and graph[i][j] != '_' and not visited[i][j]:
                check_four(i, j)

    if len(bombList) == 0:
        break
    
    # 뿌요 내리기
    for bomb in bombList:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.' # 한 칸씩 내리고 나면 맨 위 칸은 당연히 비어야 함

    time += 1

print(time)
