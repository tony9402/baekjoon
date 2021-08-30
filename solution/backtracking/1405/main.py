# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/90f99f64ed7f4b2ba7af6cba10fac4b9

import sys

def input():
    return sys.stdin.readline().rstrip()

def DFS(x,y,ct,now):
    global ans
    if ct == N:
        ans += now
        return
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if visited[dx][dy] == 0:
            visited[dx][dy] = 1
            DFS(dx,dy,ct+1,now*dir[i]/100)
            visited[dx][dy] = 0
            
arr = list(map(int, input().split()))
ans = 0
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
visited = [[0 for i in range(31)] for j in range(31)]
N = arr[0]
dir = arr[1:]
visited[14][14] = 1
DFS(14,14,0,1)
print(ans)