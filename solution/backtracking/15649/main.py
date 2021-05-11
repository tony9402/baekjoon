# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/69f68131effd4506a17fdac4b8569c6c
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [ 0 for _ in range(10) ]
used   = [ 0 for _ in range(10) ]

def dfs(cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if used[i]:
            continue
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0

dfs(0)
