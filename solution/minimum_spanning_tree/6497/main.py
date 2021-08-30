# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/b650c3b805ac4251a7a125606197836a

import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    edge = []
    total = 0
    for _ in range(m):
        x, y, w = map(int, input().split())
        edge.append([x, y, w])
        total += w
    num_edge = 0
    edge.sort(key=lambda x: -x[2])

    # Disjoint set 구성
    dis_set = [-1 for _ in range(n+1)]
    def upward(x, change_lst):
        if dis_set[x] < 0:
            return x
        change_lst.append(x)
        return upward(dis_set[x], change_lst)

    def find_root(x):
        change_lst = []
        res = upward(x, change_lst)

        for idx in change_lst:
            dis_set[idx] = res
        return res

    def union(x, y):
        x_root = find_root(x)
        y_root = find_root(y)
        if x_root != y_root: # 두 node의 root가 다르다면?
            if dis_set[x_root] < dis_set[y_root]:
                dis_set[y_root] = x_root
            if dis_set[x_root] > dis_set[y_root]:
                dis_set[x_root] = y_root
            else:
                dis_set[x_root] = -1
                dis_set[y_root] = x_root
                
    # 크루스칼 시작
    sol = 0
    while num_edge < n-1:
        x, y, w = edge.pop()
        if find_root(x) != find_root(y):
            union(x, y)
            sol += w
            num_edge += 1

    print(total - sol)
