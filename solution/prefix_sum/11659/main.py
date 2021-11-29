# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/6ada03e306dd451fbea38bfb38db2a74

import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
lst = list(map(int, input().split()))
prefix_sum = [lst[0]]
for i in range(1, n): # 누적 합 구해두기
    prefix_sum.append(prefix_sum[i-1] + lst[i])

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    if x: print(prefix_sum[y-1] - prefix_sum[x-1])
    else: print(prefix_sum[y-1])
