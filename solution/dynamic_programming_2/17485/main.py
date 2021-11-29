# Authored by : yj2221
# Co-authored by : tony9402
# Link : http://boj.kr/1b3b764580774cf799a9a9606d12fec0

import sys
def input():
    return sys.stdin.readline().rstrip()

INF = 99999999
n, m = map(int,input().split())
board = [list(map(int,input().split())) for i in range(n)]
dp = [[[INF] * m for _ in range(n)] for _ in range(3)]

for i in range(m):
    dp[0][0][i] = board[0][i]
    dp[1][0][i] = board[0][i]
    dp[2][0][i] = board[0][i]

for i in range(1, n):
    for j in range(m):
        dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j]) + board[i][j]
        if j!=m-1:
            dp[1][i][j] = min(dp[0][i-1][j+1], dp[2][i-1][j+1]) + board[i][j]
        if j!=0:
            dp[2][i][j] = min(dp[1][i-1][j-1], dp[0][i-1][j-1]) + board[i][j]

print(min(min(dp[0][n-1]),min(dp[1][n-1]), min(dp[2][n-1])))
