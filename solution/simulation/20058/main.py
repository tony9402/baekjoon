# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/f0c88b8e08204d33a7e63a384b5fdc4c
import sys
from copy import deepcopy
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dy = (-1, 1, 0, 0)
dx = ( 0, 0,-1, 1)
K, Q = map(int, input().split())
N = 1 << K

arr = list()
for i in range(N):
    arr.append(list(map(int, input().split())))

CMD = list(map(int, input().split()))

for _L in CMD:
    L = 1 << _L
    tmp = deepcopy(arr)
    for i in range(0, N, L):
        for j in range(0, N, L):
            for n in range(0, L):
                for m in range(0, L):
                    arr[i + m][j + L - 1 - n] = tmp[i + n][j + m]

    tmp = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 > y or y >= N or 0 > x or x >= N:
                    continue
                if arr[y][x] != 0:
                    cnt += 1

            if cnt < 3:
                tmp[i][j] -= 1
    arr = deepcopy(tmp)

total = 0
mx    = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        cnt = 0
        que = deque()
        que.append((i, j))
        total += arr[i][j]
        arr[i][j] = 0
        while len(que) != 0:
            cy, cx = que.popleft()
            cnt += 1
            for k in range(4):
                y = cy + dy[k]
                x = cx + dx[k]
                if 0 > y or y >= N or 0 > x or x >= N or arr[y][x] == 0:
                    continue
                que.append((y, x))
                total += arr[y][x]
                arr[y][x] = 0
        mx = max(mx, cnt)

print(f"{total}\n{mx}")
