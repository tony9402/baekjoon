# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/23af4ad30fe24df4a71cdd3db925087c
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][numbers[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] <= 0:
            continue
        for oper in (1, -1):
            temp = j + oper * numbers[i]
            if 0 <= temp < 21:
                dp[i][temp] += dp[i - 1][j]
answer = dp[N - 2][numbers[N - 1]]
print(answer)
