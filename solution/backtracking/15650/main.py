# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/afca9b0c42354f99a6578ab92e0de0a3
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [ 0 for _ in range(10) ]
used   = [ 0 for _ in range(10) ]

def dfs(idx, cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return

    for i in range(idx, N + 1):
        if used[i]:
            continue
        used[i] = 1
        choose[cnt] = i
        dfs(i + 1, cnt + 1)
        used[i] = 0

dfs(1, 0)


