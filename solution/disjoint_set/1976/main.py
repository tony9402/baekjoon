# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/a5ab5f0d45ed4e5584f0444987ba6c9a

import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

N = int(input())
M = int(input())
parent = [i for i in range(N)]
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            a = find_parent(i)
            b = find_parent(j)
            union(a,b)
ans = list(map(int, input().split()))
flag = 0
standard = ans[0] - 1
for i in range(1, len(ans)):
    if parent[standard] != parent[ans[i]-1]:
        flag = 1
        break
if not flag:
    print('YES')
else:
    print('NO')