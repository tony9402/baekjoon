# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/96e1649268004d00a43de20ff16aca62

import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x, y):
    x = find_parent(parent[x])
    y = find_parent(parent[y])
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    parent = [i for i in range(N)]
    arr = []
    ct = 0
    total = 0
    total_tree = 0
    for i in range(M):
        arr.append(list(map(int, input().split())))
        total += arr[i][2]
    arr.sort(key = lambda x : x[2])
    for i in range(M):
        x = find_parent(arr[i][0])
        y = find_parent(arr[i][1])
        if x != y:
            union(x,y)
            total_tree += arr[i][2]
            ct += 1
        if ct == N - 1:
            break
    print(total - total_tree)