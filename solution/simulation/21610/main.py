# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/709edf708bcb49e3972565b8fce5a993

import sys
from collections import deque
from copy import deepcopy

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = []
move = []
visited = [[0 for x in range(N)] for y in range(N)]
storm = []
nx = [0,-1,-1,-1,0,1,1,1]
ny = [-1,-1,0,1,1,1,0,-1]

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(M):
    move.append(list(map(int, input().split())))

storm.append((N-1, 0))
storm.append((N-1, 1))
storm.append((N-2, 0))
storm.append((N-2, 1))

for i in range(M):
    d, s = move[i][0]-1, move[i][1]
    visited = [[0 for x in range(N)] for y in range(N)]
    new_storm = []
    for j in range(len(storm)):
        dx = storm[j][0] + nx[d] * s
        dy = storm[j][1] + ny[d] * s
        if dx < 0:
            while True:
                new_dx = dx + N
                if new_dx >= N:
                    break
                dx += N
        elif dx >= N:
            while True:
                new_dx = dx - N
                if new_dx < 0:
                    break
                dx -= N
        if dy < 0:
            while True:
                new_dy = dy + N
                if new_dy >= N:
                    break
                dy += N
        elif dy >= N:
            while True:
                new_dy = dy - N
                if new_dy < 0:
                    break
                dy -= N
        new_storm.append((dx,dy))
        visited[dx][dy] = 1

    for j in range(len(new_storm)):
        arr[new_storm[j][0]][new_storm[j][1]] += 1

    save = []
    for j in range(len(new_storm)):
        ct = 0
        for z in range(1,8,2):
            dx = new_storm[j][0] + nx[z]
            dy = new_storm[j][1] + ny[z]
            if dx < 0 or dx >= N:
                continue
            if dy < 0 or dy >= N:
                continue
            if arr[dx][dy] > 0:
                ct += 1
        save.append(ct)

    for j in range(len(new_storm)):
        arr[new_storm[j][0]][new_storm[j][1]] += save[j]

    storm = []
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and arr[x][y] >= 2:
                arr[x][y] -= 2
                storm.append((x,y))

total = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            total += arr[i][j]

print(total)
