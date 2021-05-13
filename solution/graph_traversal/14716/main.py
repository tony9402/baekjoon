# Authored by : chj3748
# Co-authored by : tony9402
# Link : http://boj.kr/b5d154fcfb1c46e6a99e702c35f4eb26
import sys

def input():
    return sys.stdin.readline().rstrip()

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]
dirx = (1, 0, -1, 0, 1, 1, -1, -1)
diry = (0, 1, 0, -1, 1, -1, 1, -1)

def find_string(row, col):
    stack = [(row, col)]
    banner[row][col] = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dirx, diry):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and banner[nx][ny]:
                stack.append((nx, ny))
                banner[nx][ny] = 0
    return 1

string_cnt = 0
for i in range(M):
    for j in range(N):
        if banner[i][j]:
            string_cnt += find_string(i, j)

print(string_cnt)
