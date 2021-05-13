# // Authored by : chj3748
# // Co-authored by : tony9402
# // Link : http://boj.kr/4d17bddef7af409ebdb384693b3f96d9
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dirx = (0, 1)
diry = (1, 0)
N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    if x == N - 1 and y == N - 1:
        print('HaruHaru')
        exit(0)

    for dx, dy in zip(dirx, diry):
        nx, ny = x + dx * maps[x][y], y + dy * maps[x][y]
        if 0 <= nx < N and 0 <= ny < N:
            q.append((nx, ny))
    maps[x][y] = inf

print('Hing')
