# Authored by : yoonoh123
# Co-authored by : -
# Link : http://boj.kr/30d79301e5704acb8116ec1695832d0f

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
    
def rotateBoard(standard):
    last = board[standard][standard]
    
    # 12 ←
    for i in range(standard, M - 1 - standard):
        board[standard][i] = board[standard][i+1]
    
    # 3 ↑
    for i in range(standard, N - 1 - standard):
        board[i][M - 1 - standard] = board[i+1][M - 1 - standard]
    
    # 6 →
    for i in range(M - 1 - standard, standard, -1):
        board[N - 1 - standard][i] = board[N - 1 - standard][i - 1]
    
    # 9 ↓
    for i in range(N - 1 - standard, standard, -1):
        board[i][standard] = board[i - 1][standard]
    
    board[standard+1][standard] = last

standard = 0 # start
while standard < M // 2 and standard < N // 2:
    div = (M - standard * 2) * (N - standard * 2) - (M - ((standard+1) * 2)) * (N - ((standard+1)) * 2)
    loop = R % div # div = 현재 기준점의 사각형의 넓이 - 그 다음 기준점의 사각형의 넓이
    for i in range(loop):
        rotateBoard(standard)
    standard += 1
    
for i in range(N):
    print(*board[i])
