# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/c707bb0afebf42d3adaad7fee180a45a

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

m, n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
start = list(map(int,input().split()))
start[0]-=1
start[1]-=1
end = list(map(int,input().split()))
end[0]-=1
end[1]-=1

def move(dir):
    if dir==1:
        return 0, 1
    if dir==2:
        return 0, -1
    if dir==3:
        return 1, 0
    if dir==4:
        return -1, 0

def bfs():
    y, x, dir = start
    visit = [[[False] * n for _ in range(m)] for _ in range(5)]
    visit[dir][y][x] = True
    q = deque()
    q.append((y, x, dir, 0))
    result = 0
    while q:
        y, x, dir, cnt = q.popleft()
        if y==end[0] and x==end[1] and dir==end[2]:
            result = cnt
            break
        for i in range(1, 4):
            dy,dx = move(dir)
            ny = y + dy * i
            nx = x + dx * i
            if ny<0 or ny>=m or nx<0 or nx>=n: break
            if board[ny][nx]==1: break
            if visit[dir][ny][nx]: continue
            visit[dir][ny][nx] = True
            q.append((ny, nx, dir, cnt+1))

        for next_dir in range(1, 5):
            if dir==next_dir: continue
            if visit[next_dir][y][x]: continue
            visit[next_dir][y][x] = True
            if (dir==1 and next_dir==2) : q.append((y, x, next_dir, cnt+2))
            elif (dir==2 and next_dir==1) : q.append((y, x, next_dir, cnt+2))
            elif (dir==3 and next_dir==4) : q.append((y, x, next_dir, cnt+2))
            elif (dir==4 and next_dir==3) : q.append((y, x, next_dir, cnt+2))
            else: q.append((y, x, next_dir, cnt+1))
    return result

print(bfs())
