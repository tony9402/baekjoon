# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/73b9e168131842dd90aa2b02380cb0fa

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if lst[i][j] == 0:
            continue
        jump = lst[j][i]
        
        if j+jump < n:
            dp[j+jump][i] += dp[j][i]
        if i+jump < n:
            dp[j][i+jump] += dp[j][i]

print(dp[-1][-1])
