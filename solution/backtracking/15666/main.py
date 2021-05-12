# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/dbd389b484d4468990a877b205126f0f
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr  = sorted(list(map(int, input().split())))
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

