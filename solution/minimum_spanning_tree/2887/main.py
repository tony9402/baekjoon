# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/2e3dd1e84f754eaa90dfdd6d75692910
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

def find_parent(p):
    if p_parents[p] != p:
        p_parents[p] = find_parent(p_parents[p])
    return p_parents[p]

def union_planet(p1, p2):
    p1_parent = find_parent(p1)
    p2_parent = find_parent(p2)
    if p1_parent == p2_parent:
        return False
    if p1_parent < p2_parent:
        p_parents[p2_parent] = p1_parent
    else:
        p_parents[p1_parent] = p2_parent
    return True

N = int(input())
planets = []
p_parents = [i for i in range(N)]
edges = []

for i in range(N):
    p_info = list(map(int, input().split()))
    planets.append(p_info+[i])

for sort_n in range(3):
    planets.sort(key=lambda x: x[sort_n])
    for i in range(N - 1):
        p1x, p1 = planets[i][sort_n], planets[i][3]
        p2x, p2 = planets[i + 1][sort_n], planets[i + 1][3]
        heapq.heappush(edges, [ abs(p1x - p2x), p1, p2 ])

answer = 0
cnt = 0
while edges:
    cost, p1, p2 = heapq.heappop(edges)
    if union_planet(p1, p2):
        answer += cost
        cnt += 1
        if cnt == N - 1:
            break
print(answer)
