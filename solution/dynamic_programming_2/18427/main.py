# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/9ee437520e914410892bf9cb9b96adad

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())
students = []
for _ in range(N):
    students.append(list(map(int, input().split())))
    
dp = [0] * (H+1)
dp[0] = 1


for i in range(N):
    data = []
    for j in range(H+1):
        for k in students[i]:
            if dp[j] != 0 and j + k <= H:
                data.append((j + k, dp[j]))
    
    for height,value in data:
        dp[height] = (dp[height] + value) % 10007

print(dp[H])
