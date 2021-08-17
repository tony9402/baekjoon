# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e8d47d936e104388916666605df5778d

import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]
    
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
arr = []
ans = 0
for i in range(M):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : x[2])
for i in range(M):
    if find_parent(arr[i][0]) != find_parent(arr[i][1]):
        union(arr[i][0], arr[i][1])
        ans += arr[i][2]
print(ans)