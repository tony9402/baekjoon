import sys

def ri():
    return sys.stdin.readline().strip()

N, M = map(int, ri().split())
choose = [ 0 for _ in range(10) ]

def dfs(idx, cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(choose[idx], end=' ')
        print()
        return

    for i in range(1, N + 1):
        choose[cnt] = i
        dfs(i + 1, cnt + 1)

dfs(1, 0)

