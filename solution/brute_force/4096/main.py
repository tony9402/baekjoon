# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/b554cc74d1a24c9e9306775641121065
import sys
def input():
    return sys.stdin.readline().rstrip()

def isPalindrome(s):
    return s == s[::-1]

while True:
    N = input()
    length = len(N)
    ct = 0
    if N == '0':
        break
    elif isPalindrome(N):
        print(0)
    else:
        while True:
            if isPalindrome(N):
                print(ct)
                break
            N = str(int(N)+1)
            N = '0' * (length - len(N)) + N
            ct += 1