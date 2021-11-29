# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/5af0f7388d84485db221c368ce306c4b

import sys
def input():
    return sys.stdin.readline().rstrip()

h, w = map(int, input().split())
wall = list(map(int, input().split()))

# Numpy 없이 argmax
def argmax(a):
    return max(range(len(a)), key=lambda x: a[x])
max_idx = argmax(wall)

sol, tmp_max = 0, 0
# 가장 높은 벽 기준 왼쪽부터 벽+채울 수 있는 물 합한 면적 더하기
for i in range(max_idx+1):
    tmp_max = max(tmp_max, wall[i])
    sol += tmp_max

tmp_max = 0
# 가장 높은 벽 기준 오른쪽부터 벽+채울 수 있는 물 합한 면적 더하기
for i in range(w-1, max_idx, -1):
    tmp_max = max(tmp_max, wall[i])
    sol += tmp_max

#벽이 차지하는 면적 빼주면 정답
print(sol-sum(wall))