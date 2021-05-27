# Authored by : klm03025
# Co-authored by : -
# Link : http://boj.kr/b57f1dad96a946e48e0679872d97d024
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
result = ""

for i in range(N):
    testcase = input()
    cnt = 0
    for c in testcase:
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            result += "NO\n"
            break
    else:
        result += "YES\n" if cnt == 0 else "NO\n"

print(result)