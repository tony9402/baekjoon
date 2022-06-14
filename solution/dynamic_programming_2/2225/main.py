# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/086b59498e3a42d38560d7086414cce9

import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

dp = [1]*(n+1)
for _ in range(k-1):
    for i in range(1, n+1):
        dp[i] = (dp[i]+dp[i-1])%1000000000

print(dp[n])