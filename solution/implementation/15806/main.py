# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/211883f3485445669772b7b6bce7dbeb
        
from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, K, t = map(int, input().split())
board = [[0]*N for _ in range(N)]

molds, cleans = [], []
for _ in range(M):
    x, y = map(int, input().split())
    y -= 1
    x -= 1
    board[y][x] = 1
    molds.append([y, x])

for _ in range(K):
    x, y = map(int, input().split())
    y -= 1
    x -= 1
    cleans.append([y, x])

visit = [[[False]*N for _ in range(N)] for _ in range(2)]

def bfs(molds, t):
    next_molds = deque()
    
    dy = [-2,-2,-1,-1,1,1,2,2]
    dx = [-1,1,-2,2,-2,2,-1,1]
    while molds:
        y, x = molds.popleft()
        
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if ny>=N or ny<0 or nx>=N or nx<0: continue
            if visit[(t+1)%2][ny][nx]: continue
            visit[(t+1)%2][ny][nx] = True
            next_molds.append([ny,nx])
    return next_molds


def solution(cleans, molds):
    global board, visit
    molds = deque(molds)
    for _t in range(t):
        molds = bfs(molds, _t)
    for clean in cleans:
        y, x = clean
        if visit[(_t+1)%2][y][x]==1:
            return True
    return False

result = solution(cleans, molds)
print('YES' if result else 'NO')
