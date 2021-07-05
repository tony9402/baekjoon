# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/27c8f362bf2c4defbe77f079e9eaa89e
import sys
sys.setrecursionlimit(10000)

def input():
    return sys.stdin.readline().rstrip()

def DFS(x, y):
    arr[x][y] = 0
    for i in range(8):
        dx = nx[i] + x
        dy = ny[i] + y
        if dx < 0 or dx >= h or dy < 0 or dy >= w:
            continue
        if arr[dx][dy] == 1:
            DFS(dx,dy)

nx = [-1,-1,-1,0,1,1,1,0]
ny = [-1,0,1,1,1,0,-1,-1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    ct = 0
    for i in range(h):
        arr.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                DFS(i,j)
                ct += 1
    print(ct)
