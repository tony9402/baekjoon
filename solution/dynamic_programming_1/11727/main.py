# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/db4e4b38ee3c4264b672837fa8fff893
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 3

for i in range(3,N+1):
    dp[i] = dp[i-1] % 10007 + dp[i-2] * 2 % 10007

print(dp[N] % 10007)