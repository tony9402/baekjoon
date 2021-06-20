# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/0dd94001579e4341b3ea06ed523d2cba
import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = []
ans = set()
k = int(input())
for i in range(n):
    arr.append(input())
per = list(permutations(arr, k))
for i in range(len(per)):
    st = ''
    for j in range(len(per[i])):
        st += per[i][j]
    ans.add(st)
ans = list(ans)
print(len(ans))