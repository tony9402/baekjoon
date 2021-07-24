# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/e75629ad3348460599c12c53f64b7062
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
len = sum(arr)
total = 0
for i in arr:
    len = len - i
    total += i * len
print(total)