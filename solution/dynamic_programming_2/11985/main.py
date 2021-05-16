# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/f293bc24e6e347dba7b5aa08836171fe
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
oranges = []
inf = float('inf')
dp = [inf] * N
dp[0] = K
for idx in range(N):
    oranges.append(int(input()))
    if idx > 0:
        max_size = oranges[idx]
        min_size = oranges[idx]
        for j in range(M):
            left_idx = idx - j
            if left_idx < 0:
                break
            if max_size < oranges[left_idx]:
                max_size = oranges[left_idx]
            if min_size > oranges[left_idx]:
                min_size = oranges[left_idx]
            if left_idx - 1 >= 0:
                temp = dp[left_idx - 1] + K + (max_size - min_size) * (j + 1)
            else:
                temp = K + (max_size - min_size) * (j + 1)
            if dp[idx] > temp:
                dp[idx] = temp

print(dp[N - 1])
