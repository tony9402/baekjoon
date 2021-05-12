# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/fc8e94e5fb3f4384a7272130a0624d8d
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr  = sorted(list(map(int, input().split())))
choose = [ 0 for _ in range(10) ]

def dfs(cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return

    pre = -1
    for i in range(0, N):
        if pre == arr[i]:
            continue
        pre = arr[i]
        choose[cnt] = i
        dfs(cnt + 1)

dfs(0)
