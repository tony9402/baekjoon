# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/dd28c9dd06a54efeb12b4f72e82e8c77
import sys

def input():
    return sys.stdin.readline().strip()

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

    for i in range(0,N):
        choose[cnt] = i
        dfs(cnt + 1)

dfs(0)
