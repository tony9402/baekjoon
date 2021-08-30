# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/5c0cf17f207745eb899923dfc5881c26

import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x,y):
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if arr[dx][dy] < arr[x][y]:
                dp[x][y] += DFS(dx,dy)
    return dp[x][y]

N, M = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
dp = [[-1 for i in range(M)] for j in range(N)]
for i in range(N):
    arr.append(list(map(int, input().split())))
print(DFS(0,0))