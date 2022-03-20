# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/51782871a9344a4c98d433f233f83d20

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n+1)  # dp[i]는 i원을 만들기 위해 필요한 동전의 최소 개수

for i in range(1, n+1):
    tmp = []
    for coin in [1, 2, 5, 7]:
        if i >= coin:
            tmp.append(dp[i-coin])
    dp[i] = min(tmp) + 1

print(dp[n])
