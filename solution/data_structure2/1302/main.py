# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/8adc986ae26b461eadd65abdff3cfba9
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
book = {}
for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1

book = list(book.items())
book.sort(key = lambda x : (-x[1],x[0]))
print(book[0][0])
