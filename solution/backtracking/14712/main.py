# Pypy3
import sys

def ri():
    return sys.stdin.readline().strip()

N, M = map(int, ri().split())

# 1-index
Map = [ [ 0 for _ in range(M + 1) ] for __ in range(N + 1) ]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return
    
    y = cnt // M + 1
    x = cnt  % M + 1
    
    dfs(cnt + 1)
    if Map[y - 1][x] == 0 or Map[y][x - 1] == 0 or Map[y - 1][x - 1] == 0: # 만약 놓을 수 있는 곳이라면
        Map[y][x] = 1
        dfs(cnt + 1)
        Map[y][x] = 0

dfs(0)
print(answer)
