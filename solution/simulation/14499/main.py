# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/075c16a3aae141859d0fc937c689cae6
import sys

def input():
    return sys.stdin.readline().rstrip()
    
N, M, x, y, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
command = list(map(int, input().split()))
w, e, n, s, f, b = 0, 0, 0, 0, 0, 0

for i in command:
    if i == 1: # 동쪽으로 
        dy = y + 1
        if dy >= M:
            continue
        y += 1
        w, e, n, s, f, b = s, n, w, e, f, b
        if arr[x][y] == 0:
            arr[x][y] = s
        else:
            s, arr[x][y] = arr[x][y], 0
        print(n)
    elif i == 2: # 서쪽으로 이동
        dy = y - 1
        if dy < 0:
            continue
        y -= 1
        w, e, n, s, f, b = n, s, e, w, f, b
        if arr[x][y] == 0:
            arr[x][y] = s
        else:
            s, arr[x][y] = arr[x][y], 0
        print(n)
    elif i == 3: # 북쪽으로 이동
        dx = x - 1
        if dx < 0:
            continue
        x -= 1
        w, e, n, s, f, b = w, e, b, f, n, s
        if arr[x][y] == 0:
            arr[x][y] = s
        else:
            s, arr[x][y] = arr[x][y], 0
        print(n)
    elif i == 4: # 남쪽으로 이동
        dx = x + 1
        if dx >= N:
            continue
        x += 1
        w, e, n, s, f, b = w, e, f, b, s, n
        if arr[x][y] == 0:
            arr[x][y] = s
        else:
            s, arr[x][y] = arr[x][y], 0
        print(n)