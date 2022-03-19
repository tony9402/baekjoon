# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/674e960654484c23a1dc56715d61cd50

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

  
def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1:  # 치즈면 한 번에 녹이기 위해 멜트큐에 넣음
                    melt.append((nx, ny))
    for x, y in melt:
        cheeze[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴


n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])  # 전체 치즈 갯수 카운트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:  # 치즈를 다 녹였으면
        print(time, meltCnt, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1
