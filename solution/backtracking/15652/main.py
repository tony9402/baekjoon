# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/2a9874489cb74d7babd30d70501acff9
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [ 0 for _ in range(10) ]

def dfs(idx, cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return

    for i in range(idx, N + 1):
        choose[cnt] = i
        dfs(i, cnt + 1)

dfs(1, 0)


