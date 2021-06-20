# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e86763e30a974134ade5e3bdf6b7936d

import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(now):
    visited[now] = 1
    for i in arr[now]:
        if visited[i] == 0:
            DFS(i)

N, M = map(int, input().split())
arr = [[] for i in range(N+1)]
visited = [0] * (N+1)
ans = 0

for i in range(M):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,N+1):
    if visited[i] == 0:
        DFS(i)
        ans += 1

print(ans)