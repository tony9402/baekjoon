# Authored by : unodostre
# Co-authored by : -
# Link : http://boj.kr/8fcc7b5fbb884f788d0a0ad88803d046

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_pos():
    empty, virus = [], []
    for i in range(n):
        for j in range(m):
            # 비었다면 empty에 추가
            if arr[i][j] == 0:
                empty.append((i, j))
            # 바이러스라면 virus에 추가
            elif arr[i][j] == 2:
                virus.append((i, j))
    return empty, virus


def set_wall(comb):
    for y, x in comb:
        arr[y][x] = 1


def collapse_wall(comb):
    for y, x in comb:
        arr[y][x] = 0


def bfs(virus):
    queue = deque(virus)
    visited = [[False] * m for _ in range(n)]  # 방문 여부
    count = len(virus)  # 바이러스 개수
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            y, x = queue.popleft()
            visited[y][x] = True  # 방문 처리
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                # 지도 내에 있고
                if (0 <= ny < n) and (0 <= nx < m):
                    # 빈 공간이고 방문하지 않았다면
                    if arr[ny][nx] == 0 and not visited[ny][nx]:
                        visited[ny][nx] = True  # 방문 처리
                        queue.append((ny, nx))  # 큐에 삽입
                        count += 1  # 바이러스 개수 +1
    return count


# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

empty, virus = get_pos()  # 빈 위치, 바이러스 위치
combs = combinations(empty, 3)  # 벽을 세울 수 있는 조합

count = int(1e9)  # 바이러스 개수
# 모든 조합에 대해서
for comb in combs:
    # 벽 세우기
    set_wall(comb)

    # 바이러스 전염
    temp = bfs(virus)
    if temp < count:
        count = temp

    # 벽 허물기
    collapse_wall(comb)

# 벽의 개수 계산
wall = n * m - (len(empty) + len(virus))

# 출력
print(n * m - (count + wall + 3))
