# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/314d8f401cf149b3a24d0daf8e0a3637
import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)

def dfs(cur):
    flag = True
    visited[cur] = True
    for nei in graph[cur]:
        if visited[nei]:
            if label[cur] == label[nei]: #만약 neighbor node와 label이 같다면?
                return False # Bipartite graph가 아니다!
        else:
            label[nei] = 3 - label[cur] # 현재 node와 다른 label 저장
            flag &= dfs(nei)
    return flag
    

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    for i in range(e): # Graph 생성, Node 번호는 1번부터 저장
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [True] + [False]*v
    label = [0]*(v+1) # 모든 node의 label을 1 또는 2로 저장할 것임
    bipartite = True
    for i in range(1, v+1): # 주어지는 모든 node가 하나의 connected graph에 없을 수 있음
        if not visited[i]:
            label[i] = i
            bipartite &= dfs(i) # 각 graph마다 최소 한 번씩 dfs를 돌려야 함
        if not bipartite: break # 그 중 하나라도 bipartite가 아니면 중지
    if bipartite:
        print("YES")
    else:
        print("NO")
