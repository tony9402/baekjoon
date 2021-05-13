# Authored by : osy0056
# Co-authored by : -
# Link : http://boj.kr/da3d10e3ebc945349d778cb06444ffb1
import sys

def input():
    return sys.stdin.readline().rstrip()

tc = int(input())

dp = [0] * 15
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(tc):
    n = int(input())

    print(dp[n])
