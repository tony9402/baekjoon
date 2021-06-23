# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/8570a9ed0ba943e79fc675e72952f4a1
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
if len(arr) == 2:
    gcd = GCD(arr[0],arr[1])
    for i in range(1,gcd+1):
        if arr[0] % i == 0 and arr[1] % i == 0:
            print(i)
else:
    gcd = GCD(arr[0], arr[1])
    gcd = GCD(gcd, arr[2])
    for i in range(1,gcd+1):
        if arr[0] % i == 0 and arr[1] % i == 0 and arr[2] % i == 0:
            print(i)