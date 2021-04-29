import sys

def ri():
    return sys.stdin.readline().strip()

N, M = map(int, ri().split())
arr  = sorted(list(map(int, ri().split())))
choose = [ 0 for _ in range(10) ]
used   = [ 0 for _ in range(10) ]

def dfs(cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return

    pre = -1
    for i in range(N):
        if used[i] or pre == arr[i]:
            continue
        pre = arr[i]
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0

dfs(0)
