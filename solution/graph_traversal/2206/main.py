# Authored by : kis03160
# Co-authored by : tony9402
# Link : http://boj.kr/2cb5e18deb964794bec3e960225ad83e
from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def answer(row, col):
    global m, n

    shortest = 10000001
    q = deque()
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    q.append((row, col, 1))
    visited[row][col][1] = 1
    while q:
        r, c, is_able = q.popleft()
        for r_, c_ in direction:
            drow = r + r_
            dcol = c + c_

            if drow < 0 or dcol < 0 or drow >= n or dcol >= m:
                continue

            if visited[drow][dcol][is_able] == 0 and G[drow][dcol] == '0':
                visited[drow][dcol][is_able] = visited[r][c][is_able] + 1
                q.append((drow, dcol, is_able))

            elif is_able == 1 and G[drow][dcol] == '1':
                visited[drow][dcol][0] = visited[r][c][1] + 1
                q.append((drow, dcol, 0))


    shortest = visited[n - 1][m - 1]
    return_val = None
    if shortest[0] == 0 and shortest[1] == 0:
        return_val = -1
    else:
        if shortest[0] > shortest[1]:
            return_val = shortest[1]
            if return_val == 0:
                return_val = shortest[0]
        else:
            return_val = shortest[0]
            if return_val == 0:
                return_val = shortest[1]

    return return_val

n, m = map(int, input().split())

G = []
walls = []
for i in range(n):
    x = []
    temp = input()
    for j in range(m):
        if temp[j] == '1':
            walls.append((i, j))
            x.append('1')
        else:
            x.append('0')
    G.append(x)

print(answer(0, 0))
