# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/eca68e03c7f640158b9c6a6841997682

import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x,y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

N = int(input())
parent = [i for i in range(N+1)]
arr = []
ans = []
total = 0
ct = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans.append((i,j,arr[i][j]))
ans.sort(key = lambda x : x[2])
for i in range(N*(N-1)):
    a,b = find_parent(ans[i][0]), find_parent(ans[i][1])
    if a != b:
        union(a,b)
        total += ans[i][2]
        ct += 1
    if ct == N-1:
        break
print(total)