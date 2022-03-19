# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/0dfe13fd2bf04a1e850ae2707c79076f

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    air = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    melt = set()
    while air:
        x, y = air.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheeze[nx][ny]:  # 치즈라면
                    melt.add((nx, ny))
                    cheeze[nx][ny] += 1
                elif not cheeze[nx][ny]:  # 공기라면
                    air.append((nx, ny))
                    visited[nx][ny] = 1
    meltCnt = 0
    for x, y in melt:
        if cheeze[x][y] > 2:  # 두 면 이상이 공기와 접촉한 치즈 녹이기
            cheeze[x][y] = 0
            meltCnt += 1
        else:  # 한 면만 접촉한 치즈 원상태로 돌려놓기
            cheeze[x][y] = 1
    return meltCnt


n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])  # 치즈 전체 개수 카운팅

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    meltCnt = bfs(0, 0)  # 녹인 치주 개수 리턴받기
    cnt -= meltCnt
    if cnt == 0:  # 치즈 다 녹았으면 종료
        print(time)
        break
    time += 1
