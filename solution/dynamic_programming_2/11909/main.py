# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/a7949813f6e74a918f1f18b458ea5f8c
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

inf = float('inf')
n = int(input())
prison = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf] * n for _ in range(n)]
dp[0][0] = 0
dirx = [1, 0]
diry = [0, 1]

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for dx, dy in zip(dirx, diry):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            cost = prison[nx][ny] - prison[x][y] + 1
            if cost < 1:
                cost = 0
            if dp[nx][ny] > dp[x][y] + cost:
                q.append((nx, ny))
                dp[nx][ny] = dp[x][y] + cost

print(dp[n - 1][n - 1])