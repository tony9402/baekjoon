# Authored by : gusdn3477
# Co-authored by : tony9402
# Link : http://boj.kr/8a53cdacfc6340c894fb47257232f244
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def checkMap():
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if arr[z][i][j] == 0:
                    return False
    return True

def BFS():
    while queue:
        q = queue.popleft()
        z, x, y = q[0]
        for i in range(6):
            dx = x + nx[i]
            dy = y + ny[i]
            dz = z + nz[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M or dz < 0 or dz >= H:
                continue
            if arr[dz][dx][dy] == 0:
                arr[dz][dx][dy] = 1
                queue.append(((dz,dx,dy), q[1]+1))

    if checkMap():
        return q[1]
    return -1

M, N, H = map(int, input().split())
arr = []
nx = [-1,0,1,0,0,0]
ny = [0,-1,0,1,0,0]
nz = [0,0,0,0,-1,1]

queue = deque()
arr = [ [ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ]

for z in range(H):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == 1:
                arr[z][i][j] = 1
                queue.append(((z,i,j),0))
ans = BFS()
print(ans)
