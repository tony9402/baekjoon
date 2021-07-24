# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/fd10df28858644eebc6b4ffd042c2d83
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    a,b = input().split()
    total = int(a,2) + int(b,2)
    print(bin(total)[2:])