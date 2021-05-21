# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/25c02a4ea33e493f9f1320165f1a5f95
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = meetings[0][2]
    elif i == 1:
        dp[1] = max(meetings[1][2], dp[0])
    else:
        dp[i] = max(dp[i-2] + meetings[i][2], dp[i-1])

print(dp[N - 1])