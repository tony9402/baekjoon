# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/5be3726ed4ca4231bc7773980ae90a6e

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

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

total = 0
total_tree = 0
arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : x[2])
for i in range(M):
    a = find_parent(arr[i][0])
    b = find_parent(arr[i][1])
    total += arr[i][2]
    if a != b:
        union(a,b)
        total_tree += arr[i][2]

for i in range(1, N+1):
    find_parent(i)

if parent.count(parent[1]) == N:
    print(total - total_tree)
else:
    print(-1) 
