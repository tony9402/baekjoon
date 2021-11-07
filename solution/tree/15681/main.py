# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/74cde7f86d27498c9a3a724e4ddc206f
import sys
def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000) # 꼭 걸어주도록 하자....

n, r, q = map(int, input().split())
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

    n_c = 0 # cur를 root로 하는 subtree의 node 개수
    for c in tree[cur]:
        if c != parent: # 각 child를 root로 하는 subtree의 node 개수 추가
            n_c += dfs(c, cur)
    num_child[cur] = n_c+1 # 본인 추가
    return n_c+1

dfs(r, -1)

for _ in range(q):
    print(num_child[int(input())])