# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/62858e6576584934b6d2db90001acd5b

import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**4)

n, h, d = map(int, input().split())

visit = [[False] * n for _ in range(n)]
umbs = []
for i in range(n):
    _str = input()
    for j in range(n):
        if _str[j] == 'U':
            umbs.append([i, j])
        if _str[j] == 'S':
            start = [i, j]
        if _str[j] == 'E':
            end = [i, j]
answer = 99999999

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def dfs(cur):
    global answer, n
    y, x, health, durability, cnt = cur
    dist = abs(end[0] - y) + abs(end[1] - x)
    if dist <= health + durability:
        answer = min(answer, cnt + dist)
        return
    else:
        for umb in umbs:
            uy, ux = umb
            if visit[uy][ux]: continue
            dist2 = abs(uy - y) + abs(ux - x)
            if dist2 - 1 >= health + durability: continue
            visit[uy][ux] = True
            if dist2 <= durability:
                dfs((uy, ux, health, d, cnt + dist2))
            else:
                dfs((uy, ux, health + durability - dist2, d, cnt + dist2))
            visit[uy][ux] = False


dfs((start[0], start[1], h, 0, 0))
if answer == 99999999:
    print(-1)
else:
    print(answer)
