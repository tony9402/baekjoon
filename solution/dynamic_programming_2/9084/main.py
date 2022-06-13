# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/197f8d7457bd4f29a10e8130a80292d3

import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    
    dp = [0]*(m+1)
    dp[0] = 1 #초깃값
    
    for coin in lst:
        for i in range(m+1):
            # coin원을 보고 있을 때 i원을 만드는 방법: i-coin원을 만드는 방법에 coin원 추가
            # -> 기존 i원을 만드는 방법 + i-coin원을 만드는 방법
            if i >= coin: dp[i] += dp[i-coin]
    
    print(dp[m])