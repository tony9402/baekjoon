# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/f23ea6f1ea594b6f9c8100fd1ef41633

import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def DFS(x, ar):
    global ct
    ct += pop[x]
    visited[x] = 1
    for i in range(1, N+1):
        if i in arr[x] and visited[i] == 0 and i in ar:
            visited[i] = 1
            DFS(i, ar)
    return ct
N = int(input())
pop = list(map(int, input().split()))
pop.insert(0,0)
arr = [[] for i in range(N+1)]
stan = [i for i in range(1,N+1)]
MIN = 1e9
for i in range(1, N+1):
    t = list(map(int, input().split()))
    arr[i] = t[1:]
for i in range(1, N):
    comb_list = list(combinations(stan, i))
    for comb in comb_list:
        visited = [0] * (N+1)
        remain = [j for j in range(1,N+1) if j not in comb]
        ct = 0
        first = DFS(comb[0], comb)
        ct = 0
        second = DFS(remain[0], remain)
        if visited.count(1) == N:
            MIN = min(MIN, abs(first - second))
if MIN == 1e9:
    print('-1')
else:
    print(MIN)