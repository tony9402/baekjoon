# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/74cde7f86d27498c9a3a724e4ddc206f
import sys
def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000) # 꼭 걸어주도록 하자.... (Python 인 경우)

n, root, query = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1): # Tree 생성
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

num_child = [0]*(n+1)

def dfs(cur, parent):
    if len(tree[cur]) == 1 and parent != -1: # Leaf node라면
        num_child[cur] = 1
        return 1

    n_sub = 0 # cur를 root로 하는 subtree의 node 개수
    for child in tree[cur]:
        if child != parent: # 각 child를 root로 하는 subtree의 node 개수 추가
            n_sub += dfs(child, cur)
    num_child[cur] = n_sub + 1 # 본인 추가
    return n_sub + 1

dfs(root, -1)

for _ in range(query):
    print(num_child[int(input())])
