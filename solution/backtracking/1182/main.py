# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/1938989c82c1488282cdb2c22d4a9e17
import sys

def input():
    return sys.stdin.readline().rstrip()

def backTracking(idx):
    global ans
    if len(poc) >= N:
        if sum(poc) == S:
            ans += 1
        return
    else:
        if sum(poc) == S and poc:
            ans += 1
        for i in range(idx,N):
            poc.append(arr[i])
            backTracking(i+1)
            poc.pop()
            
N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
poc = []
ans = 0
backTracking(0)
print(ans)