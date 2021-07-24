# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/6b74718335d14780a6213de8a6b33e42
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * (N+1)
for i in range(N):
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))