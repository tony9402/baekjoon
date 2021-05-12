# Authored by : osy0056
# Co-authored by : -
# Link : http://boj.kr/60f2feff1f9848acacf30906c56b9b09
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
dp = [-1]*(n + 10)

dp[1] = 0
for i in range(1, n + 1):
    cur_min = dp[i - 1] + 1
    if i % 3 == 0:
        cur_min = min(cur_min, dp[i // 3] + 1)
    if i % 2 == 0:
        cur_min = min(cur_min, dp[i // 2] + 1)
    dp[i] = cur_min

print(dp[n])
