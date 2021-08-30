# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/4c2449f200e440f39d4ba8e1e71601b6

import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = set([int(input()) for _ in range(n)]) #중복 동전 제거
dp = [0]*(k+1)

for i in range(1, k+1):
    possible = []
    for c in coin:
        if i-c >= 0 and dp[i-c] >= 0: # i-c원 경우에 c원 동전을 추가해서 i원을 만들 수 있는 경우
            possible.append(dp[i-c])
    if possible:
        dp[i] = min(possible) + 1 # optimal 값 + 1
    else:
        dp[i] = -1 #불가능!

print(dp[k])
