# // Authored by : chj3748
# // Co-authored by : -
# // Link : http://boj.kr/28603d67d3014c79af724768c75865af
import sys

def input():
    return sys.stdin.readline().rstrip()

def origami(start, end):
    if start == end:
        return True
    mid = (start + end) // 2
    sign = True
    for i in range(start,mid):
        if status[i] == status[end-i]:
            sign = False
            break
    if sign:
        return origami(start, mid - 1) and origami(mid + 1, end)
    else:
        return False

for T in range(int(input())):
    status = list(map(int, input()))
    if origami(0, len(status) - 1):
        answer = 'YES'
    else:
        answer = 'NO'
    print(answer)