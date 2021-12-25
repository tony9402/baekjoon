# Authored by : yj2221
# Co-authored by : tony9402
# Link : http://boj.kr/069cb935ee08462280976f02691b40ca

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())

students = []
for _ in range(N):
    students.append(list(map(int, input().split())))
    
dp = [1] + [0] * (H+1)

for i in range(N):
    for j in range(H, -1, -1):
        for k in students[i]:
            if j - k >= 0:
                dp[j] = (dp[j] + dp[j - k]) % 10007

print(dp[H])
