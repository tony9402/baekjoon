# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/3d9ff337b9bc420a975cf6783b298212

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = [int(input()) for _ in range(n)]

if n > 3:
    dp = [lst[0], lst[0]+lst[1], max(lst[0], lst[1])+lst[2]] # 3번째 칸까지는 먼저 구하기
    for i in range(3, n):
        next_max = max(dp[i-2], dp[i-3]+lst[i-1]) # max(2칸 전에서 i번째 경우, 3칸-1칸 전 밟고 i번째 오는 경우)
        dp.append(next_max+lst[i])
    print(dp[-1])
else:
    print(sum(lst)) #2칸 이하면 모두 밟는게 최대

