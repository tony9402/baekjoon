# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/69e732906ee9469bbd233ff0ed09bafb

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dis_set = [-1]*(n+1)

#Disjoint set 관련 함수
def upward(x, update_lst):
    if dis_set[x] < 0: # 해당 disjoint set의 최상단 root를 찾음
        return x
    # x가 root가 아니라면 update_lst에 추가하고 root를 찾아감
    update_lst.append(x)
    return upward(dis_set[x], update_lst)

def find(x):
    update_lst = [] # x가 속한 disjoint set에서 path compression을 위해 root update가 필요한 node set
    root = upward(x, update_lst) # x가 속한 disjoint set의 root
    for idx in update_lst: # Path compression
        dis_set[idx] = root
    return root

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root: #두 node의 root가 다르다면 -> 합쳐야 함
        dis_set[y_root] = x_root


for _ in range(m):
    oper, x, y = map(int, input().split())
    if oper: # Check
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")

    else: # Union
        union(x, y)
