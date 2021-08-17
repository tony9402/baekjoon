# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/726b58947cd144afa6fa9abf2b491ac7
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
apple = [0] * 10005

K = int(input())

for i in range(K):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1
L = int(input())
nx = [1,0,-1,0]
ny = [0,1,0,-1]
d = 1
time = 1

queue = deque()
queue.append((0,0))
for i in range(L):
    a,b = input().split()
    apple[int(a)] = b

while True:
    x,y = queue.pop()
    dx = nx[d] + x
    dy = ny[d] + y
    if (dx, dy) in queue or dx < 0 or dx >= N or dy < 0 or dy >= N:
        break
    if arr[dx][dy] == 1:
        arr[dx][dy] = 0
        queue.append((x,y))
        queue.append((dx,dy))
    else:
        queue.append((x,y))
        queue.append((dx,dy))
        queue.popleft()
    if apple[time] == 'L':
        d = (d+1) % 4
    elif apple[time] == 'D':
        d = (d+3) % 4
    time += 1

print(time)
