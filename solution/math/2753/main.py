# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/8321cffd959748c981d1cb359cccee9d
import sys

def input():
    return sys.stdin.readline().rstrip()

year = int(input())

print(1 if not year % 4 and (year % 100 or not year % 400) else 0)
