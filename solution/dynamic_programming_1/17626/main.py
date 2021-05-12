# Authored by : osy0056
# Co-authored by : -
# Link : http://boj.kr/782a2e02166c4b5cba7c42b19d55a7e5
import math


[n] = [*map(lambda x: int(x), input().split())]
dp = [0]*50001
INF = float('inf')

dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    min_value = INF
    for k in range(1, math.floor(math.sqrt(k))+1):
        min_value = min(min_value, dp[i-k*k])
    dp[i] = min_value+1
print(dp[n])
