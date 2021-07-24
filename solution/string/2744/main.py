# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/39641966833845ec931ab403fc15026d
import sys
def input():
    return sys.stdin.readline().rstrip()

word = input()
ans = ''
for i in word:
    if i.islower():
        ans += i.upper()
    else:
        ans += i.lower()
print(ans)