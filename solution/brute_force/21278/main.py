# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/b52664ec81c3495db8b8091cd12f95d5

from itertools import combinations
from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start1, start2, graph, N):
    result = [99999999 for _ in range(N+1)]
    result[0] = 0 # 인덱스 0은 더미
    result[start1] = 0
    result[start2] = 0
    q = deque()
    q.append((start1, 0))
    q.append((start2, 0))
    visit = set()
    visit.add(start1)
    visit.add(start2)
    while q:
        if len(visit) == N:
            break
        cur, dist = q.popleft()
        for nxt in graph[cur]:
            if nxt in visit: continue
            visit.add(nxt)
            q.append((nxt, dist + 1))
            result[nxt] = dist + 1
    return sum(result)


def solution(graph, N):
    candidate = [i for i in range(1, N+1)]
    answer = 99999999
    fin_store1 = N+1
    fin_store2 = N+1
    for comb in combinations(candidate, 2):
        store1, store2 = comb
        result = bfs(store1, store2, graph, N)
        if answer > result:
            fin_store1 = store1
            fin_store2 = store2
            answer = result
        elif answer == result:
            if fin_store1 > store1:
                fin_store1 = store1
                fin_store2 = store2
                answer = result
            elif fin_store1 == store1:
                if fin_store2 > store2:
                    fin_store1 = store1
                    fin_store2 = store2
                    answer = result

    return ' '.join(map(str, [fin_store1, fin_store2, answer * 2]))

print(solution(graph, N))
