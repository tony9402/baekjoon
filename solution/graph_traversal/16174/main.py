# // Authored by : chj3748
# // Co-authored by : -
# // Link : http://boj.kr/4d17bddef7af409ebdb384693b3f96d9
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')
q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for dx, dy in ((0, 1), (1, 0)):
        nx, ny = x + dx * map[x][y], y + dy * map[x][y]
        if 0 <= nx < N and 0 <= ny < N:
            if nx == N - 1 and ny == N - 1:
                print('HaruHaru')
                sys.exit(0)
            q.append((nx, ny))
    map[x][y] = inf
print('Hing')
