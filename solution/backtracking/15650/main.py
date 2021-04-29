import sys

def ri():
    return sys.stdin.readline().strip()

N, M = map(int, ri().split())
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


