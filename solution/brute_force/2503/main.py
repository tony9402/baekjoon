# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/4e0ef6629dd34e659f1b3d6d470ccc41
import sys

def input():
    return sys.stdin.readline().rstrip()

def isDifferentAndNotZero(num):
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        return False
    if '0' in num:
        return False
    return True

def baseball(num):
    flag = 0
    for i in range(N):
        strike, ball = 0,0
        for j in range(3):
            if num[j] == arr[i][0][j]:
                strike += 1
        if num[0] == arr[i][0][1] or num[0] == arr[i][0][2]:
            ball += 1
        if num[1] == arr[i][0][0] or num[1] == arr[i][0][2]:
            ball += 1
        if num[2] == arr[i][0][0] or num[2] == arr[i][0][1]:
            ball += 1
        if strike == arr[i][1] and ball == arr[i][2]:
            flag += 1
    if flag == N:
        return True
    else:
        return False

N = int(input())
arr = []
poc = []
ans = 0

for i in range(N):
    num, strike, ball = input().split()
    arr.append([num, int(strike), int(ball)])

for i in range(123,988):
    if isDifferentAndNotZero(str(i)) and baseball(str(i)):
        ans += 1
print(ans)