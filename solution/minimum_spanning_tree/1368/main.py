# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/aa071582c18b4cb1acaa18950654ff3e
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dig_costs = [int(input()) for _ in range(N)]
link_costs = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N + 1))

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_set(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

edges = []
for i in range(N):
    for j in range(i + 1, N):
        heapq.heappush(edges, [link_costs[i][j], i+1, j+1])
    heapq.heappush(edges, [dig_costs[i], 0, i + 1])

link_cnt = 0
total = 0
while edges:
    if link_cnt == N:
        break
    cost, n1, n2 = heapq.heappop(edges)
    p_n1 = find_parent(n1)
    p_n2 = find_parent(n2)
    if p_n1 != p_n2:
        union_set(n1, n2)
        total += cost
        link_cnt += 1

print(total)
