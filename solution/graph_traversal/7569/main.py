# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/8a53cdacfc6340c894fb47257232f244
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def checkMap():
    for i in range(H):
        for j in range(N):
            for z in range(M):
                if arr[i][j][z] == 0:
                    return False
    return True

def BFS():
    while queue:
        q = queue.popleft()
        z,x,y = q[0][0], q[0][1], q[0][2]
        for i in range(2):
            dz = z + nz[i]
            if dz < 0 or dz >= H:
                continue
            if arr[dz][x][y] == 0:
                arr[dz][x][y] = 1
                queue.append(((dz, x, y), q[1]+1))
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if arr[z][dx][dy] == 0:
                arr[z][dx][dy] = 1
                queue.append(((z,dx,dy), q[1]+1))

    if checkMap():
        return q[1]
    return -1

M, N, H = map(int, input().split())
arr = []
nx = [-1,0,1,0]
ny = [0,-1,0,1]
nz = [-1,1]
queue = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)

for i in range(H):
    for j in range(N):
        for z in range(M):
            if arr[i][j][z] == 1:
                arr[i][j][z] = 1
                queue.append(((i,j,z),0))
ans = BFS()
print(ans)