import sys

def ri():
    return sys.stdin.readline().strip()

N, M = map(int, ri().split())
arr  = sorted(list(map(int, ri().split())))
choose = [ 0 for _ in range(10) ]

def dfs(idx, cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return

    pre = -1
    for i in range(idx, N):
        if pre == arr[i]:
            continue
        pre = arr[i]
        choose[cnt] = i
        dfs(i, cnt + 1)

dfs(0, 0)

