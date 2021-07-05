# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7d4da3364b4d4735b5f99d946b785fff
import sys
def input():
    return sys.stdin.readline().rstrip()

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

s = input()
t = input()
gcd = GCD(len(s),len(t))
lcm = len(s) * len(t) // gcd
s = s * (lcm // len(s))
t = t * (lcm // len(t))
if s == t:
    print(1)
else:
    print(0)
