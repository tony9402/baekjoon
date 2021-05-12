# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/7bbdc54527b2456d9e1e829834a2ece2
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

    for i in range(idx,N):
        choose[cnt] = i
        dfs(i, cnt + 1)

dfs(0, 0)

