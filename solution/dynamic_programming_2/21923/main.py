# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/33f73b2bfd3a443fa03f4e9f240b41a1

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

INF = 1e10
dp = [[[-INF] * m for _ in range(n)] for _ in range(2)]

# up
dp[0][n-1][0] = board[n-1][0]
for y in range(n-1, -1 ,-1):
    for x in range(m):
        if y+1<n:
            dp[0][y][x] = max(dp[0][y][x], dp[0][y+1][x] + board[y][x])
        if x-1>=0:
            dp[0][y][x] = max(dp[0][y][x], dp[0][y][x-1] + board[y][x])

# down
dp[1][n-1][m-1] = board[n-1][m-1]
for y in range(n-1, -1 ,-1):
    for x in range(m-1, -1, -1):
        if y+1<n:
            dp[1][y][x] = max(dp[1][y][x], dp[1][y+1][x] + board[y][x])
        if x+1<m:
            dp[1][y][x] = max(dp[1][y][x], dp[1][y][x+1] + board[y][x])

answer = -INF
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[0][i][j] + dp[1][i][j])

print(answer)
