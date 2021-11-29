# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/bf6009039d6b410291eb253279ce0c8f

from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

r, c = map(int, input().split())
board = [[-1] * (c+2) for _ in range(r+2)]
visit = [[False] * (c+2) for _ in range(r+2)]
q = deque()
fire_q = deque()
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(1,r+1):
    line = input()
    for j in range(1,c+1):
        if line[j-1]=='#': board[i][j] = 1
        elif line[j-1]=='.': board[i][j] = 0
        elif line[j-1]=='J': 
            board[i][j] = 0
            q.append([i,j])
        elif line[j-1]=='F': 
            board[i][j] = 2
            fire_q.append([i,j])

def check(cur, board):
    y, x = cur
    return board[y][x] == -1

def bfs(q, cnt):
    global r, c
    next_q = deque()
    while q:
        y, x = q.popleft()
        if board[y][x] == 2: continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny<0 or ny>=r+2 or nx<0 or nx>=c+2: continue
            if board[ny][nx] == 1 or board[ny][nx] == 2: continue
            if visit[ny][nx]: continue
            if check((ny,nx), board):
                return True, next_q
            next_q.append([ny, nx])
            visit[ny][nx] = True
    return False, next_q

def fire_bfs(q):
    global r, c
    next_q = deque()
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny<=0 or ny>=r+1 or nx<=0 or nx>=c+1: continue
            if board[ny][nx] == 1 or board[ny][nx] == 2: continue
            next_q.append([ny, nx])
            board[ny][nx] = 2
    return next_q

def solution():
    global q, fire_q
    cnt = 0
    while True:
        cnt += 1
        chk, q = bfs(q, cnt)
        if chk:
            return cnt
        if not q:
            return 'IMPOSSIBLE'
        fire_q = fire_bfs(fire_q)
    return 'IMPOSSIBLE'

print(solution())
