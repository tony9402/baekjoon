# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/285536cac4ee473eaf9d01b6c6540fc6
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
total = []
ans = 0
day = 0
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(n):
    total.append([arr[i],arr2[i]])
total.sort(key = lambda x : (x[1], -x[0]))
for i in range(n):
    ans += total[i][0] + total[i][1] * day
    day += 1
print(ans)