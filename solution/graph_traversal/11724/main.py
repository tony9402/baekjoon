# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/38f92898805e44cf8212e2107237c9d3

import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x):

    visited[x] = 1
    
    for i in range(1,N+1):
        if i in arr[x] and visited[i] == 0:
            DFS(i)

N, M = map(int, input().split())
arr = [[] for i in range(N+1)]
visited = [0] * (N+1)
ct = 0

for i in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for i in range(1,N+1):
    
    if visited[i] == 0:
        DFS(i)
        ct += 1
        
print(ct)