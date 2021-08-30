# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/549472cf36d2472cb68fd6a6856bea25

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
t = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for idx in range(1, n):
    tree[t[idx]].append(idx) # 트리 생성

# time[v] = v를 root로 하는 subtree에 정보를 모두 전달하는데 걸리는 시간
time = [False]*n

def dp(v):
    child_t = []
    for nei in tree[v]:
        # Leaf까지 내려감
        dp(nei)
        # 각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음
        child_t.append(time[nei])
    if not tree[v]:
        # Child가 없으면 0
        child_t.append(0)

    child_t.sort(reverse=True)
    # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    need_time = [child_t[i] + i + 1 for i in range(len(child_t))]
    time[v] = max(need_time) # 그 중에 가장 오래 걸리는 시간을 assign
    
dp(0)
print(time[0]-1) # Root node에 정보 전달하는 시간은 없으니 1빼기
