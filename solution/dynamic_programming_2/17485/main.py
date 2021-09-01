# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/8a15adcdd9e942358989f9e571fd7864

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

dp = [[[99999999] * m for _ in range(n)] for _ in range(3)]
for i in range(m):
    dp[0][0][i] = board[0][i]
    dp[1][0][i] = board[0][i]
    dp[2][0][i] = board[0][i]

for i in range(1, n):
    for j in range(m):
        if j==0:
            dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j]) + board[i][j]
            dp[1][i][j] = min(dp[0][i-1][j+1], dp[2][i-1][j+1]) + board[i][j]
            continue
        if j==m-1:
            dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j]) + board[i][j]
            dp[2][i][j] = min(dp[1][i-1][j-1], dp[0][i-1][j-1]) + board[i][j]
            continue
        dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j]) + board[i][j]
        dp[1][i][j] = min(dp[0][i-1][j+1], dp[2][i-1][j+1]) + board[i][j]
        dp[2][i][j] = min(dp[0][i-1][j-1], dp[1][i-1][j-1]) + board[i][j]

print(min(min(dp[0][n-1]),min(dp[1][n-1]), min(dp[2][n-1])))