# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/d903976eaa454c208a0a75092a20d1c6

from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

board = [list(input()) for _ in range(8)]

def bfs(board):
    end = (0,7)
    que = deque()
    que.append((7,0,0))
    visit = [[[False] * 8 for _ in range(8)] for _ in range(9)]
    visit[0][7][0] = True
    dy = [0,0,0,-1,1,-1,1,-1,1]
    dx = [0,-1,1,0,0,-1,1,1,-1]
    result = 0
    while que:
        y,x,time = que.popleft()
        if y==end[0] and x==end[1]:
            result = 1
            break
        for i in range(9):
            ny, nx = y + dy[i], x + dx[i]
            ntime = min(time + 1, 8)
            if ny<0 or ny>=8 or nx<0 or nx>=8: continue
            if ny-time>=0 and board[ny-time][nx]=='#': continue
            if ny-ntime>=0 and board[ny-ntime][nx]=='#': continue
            if visit[ntime][ny][nx]: continue
            visit[ntime][ny][nx] = True
            que.append((ny,nx,ntime))
    return result

print(bfs(board))
