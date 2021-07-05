# Authored by : gusdn3477
# Co-authored by : tony9402
# Link : http://boj.kr/aef57ade1e5c4c6e90f08a159fe96ca2
import sys

def input():
    return sys.stdin.readline().rstrip()

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

n = int(input())
arr = list(map(int, input().split()))
outputs = list()

gcd = arr[0]
for i in range(1, n):
    gcd = GCD(gcd, arr[i])

x = 1
while x * x <= gcd:
    if gcd % x == 0:
        outputs.append(x)
        if x * x != gcd:
            outputs.append(gcd // x)
    x += 1

outputs.sort()
print(*outputs)
