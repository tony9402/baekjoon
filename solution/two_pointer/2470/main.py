# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/ed73f7e0f51243299f3b032a395825f5

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
liquid = sorted(list(map(int, input().split())))

ans = 1e10
ans_list = []
start, end = 0, n - 1

while start < end:
    val = liquid[start] + liquid[end]
    if abs(val) < abs(ans):
        ans = val
        ans_list = [liquid[start], liquid[end]]
    if val < 0:
        start += 1
    else:
        end -= 1

print(ans_list[0], ans_list[1])
