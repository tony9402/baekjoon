# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/ed73f7e0f51243299f3b032a395825f5

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
liquid = sorted(list(map(int, input().split())))

ans = 10e9 + 1
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

print(' '.join(map(str, ans_list)))
