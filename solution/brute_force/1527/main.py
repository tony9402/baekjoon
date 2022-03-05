# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/116cc6e1b10245e892ef42092eaff5c5

import sys
from itertools import product
def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
x = len(str(a))
y = len(str(b))

cnt = 0

for i in range(x, y+1):
    lst = list(product([4, 7], repeat=i))
    for num in lst:
        n = int(''.join(map(str, num)))
        if a <= n <= b:
            cnt += 1

print(cnt)
