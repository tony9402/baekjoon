# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/f4bdc1e4d3f34003a1080645069b0ee7

import sys
def input():
    return sys.stdin.readline().rstrip()

dp = ['' for _ in range(1001)]
dp[1] = 'SK'

for i in range(1,1000):
    if dp[i]=="SK":
        if dp[i+1]=='':
            dp[i+1] = 'CY'
        if i+3<1000:
            dp[i+3] = 'CY'
    elif dp[i]=='CY':
        if dp[i+1]=='':
            dp[i+1] = 'SK'
        if i+3<1000:
            dp[i+3] = 'SK'

print(dp[int(input())])