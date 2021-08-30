# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/3e256d935b4e4fe3a887d16fbcb8abef

import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000000)

n = int(input())
tree = [[] for _ in range(n+1)]

mark = list(map(int, input().split()))
for idx in range(len(mark)):
    tree[mark[idx]].append(idx+2)

stat = list(map(int, input().split()))

# dp_mat[v] = [v 포함, v 미포함]
dp_mat = [[0,0] for _ in range(n+1)]
# print(stat)
def dp(v):
    con = 0
    for nei in tree[v]:
        dp(nei)

        # Node v를 사용하지 않는 경우 -> max(dp_mat[nei]) 선택
        # nei가 멘토든 아니든 상관 없이 가장 큰 경우만 가져오면 됨
        dp_mat[v][1] += max(dp_mat[nei][0], dp_mat[nei][1])

        # Node v를 사용하는 경우 -> 취사선택이 필요함!
        # 이 경우 nei 중 하나 x를 선택해서 v의 멘티로 삼게 됨
        #   x를 제외한 나머지 nei는 max(dp_mat[nei]) 취사선택
        # x를 멘티로 삼는 경우, x가 멘토인 경우와 아닌 경우를 고려해야 함
        #   dp_mat[v][1] 연산 시 dp_mat[x][1](x 미포함)을 사용하면 문제 없음
        #   만약 dp_mat[nei][0]을 사용했다면 x의 멘토 관계를 해제하고 v의 멘티로 삼아야 함
        #     이 경우 무조건 dp_mat[x][0] 대신 dp_mat[x][1]을 사용해야 함
        #     dp_mat[v][1]에 영향이 가게 됨 -> 이 영향을 con으로 계산, con을 가장 크게 만드는 x 선택
        con = max(con, stat[v-1]*stat[nei-1] - max(dp_mat[nei][0]-dp_mat[nei][1], 0))
    dp_mat[v][0] = dp_mat[v][1]+con

dp(1)
print(max(dp_mat[1]))
