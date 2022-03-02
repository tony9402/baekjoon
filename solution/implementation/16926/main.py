# Authored by : yoonoh123
# Co-authored by : -
# Link : http://boj.kr/9084ea381ed04a499c70f105eab3e286

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
    
def rotateBoard(standard):
    last = board[standard][standard]
    
    for i in range(standard, M - 1 - standard):
        board[standard][i] = board[standard][i+1]
    
    for i in range(standard, N - 1 - standard):
        board[i][M - 1 - standard] = board[i+1][M - 1 - standard]
        
    for i in range(M - 1 - standard, standard, -1):
        board[N - 1 - standard][i] = board[N - 1 - standard][i - 1]
        
    for i in range(N - 1 - standard, standard, -1):
        board[i][standard] = board[i - 1][standard]
    
    board[standard+1][standard] = last

for _ in range(R):
    standard = 0 # start
    while standard < M // 2 and standard < N // 2:
        rotateBoard(standard)
        standard += 1

for i in range(N):
    print(*board[i])
