# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/e0632ef09f52468099305ed41cd7dec7

import sys
def input():
    return sys.stdin.readline().rstrip()

adr = list(input().split(':'))

if adr.count(''):
    while len(adr) > 8:
        del adr[adr.index('')]
    while len(adr) < 8:
        adr.insert(adr.index(''), '0000')

for i in range(len(adr)):
    if len(adr[i]) < 4:
        adr[i] = '0'*(4-len(adr[i])) + adr[i]

print(*adr, sep=':')
