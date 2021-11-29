# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/18c501c01b3d4d91aa311c9c4d952e67

import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
rocks = list(map(int, input().split()))
dp = [99999999] * n
dp[0] = 0
for i in range(n-1):
    if dp[i]>k:
        continue
    for j in range(i+1, n):
        need = (j-i) * (1 + abs(rocks[i]-rocks[j]))
        dp[j] = min(dp[j], need)
        
if dp[n-1]>k:
    print('NO')
else:
    print('YES')
