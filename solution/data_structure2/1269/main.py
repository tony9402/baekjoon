# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/73b320e09628425c8d29b3c81287a865
import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

len_a, len_b = map(int, input().split())
dict_a = defaultdict(int)

for number in map(int, input().split()):
    dict_a[number] = 1

cnt = 0

for number in map(int, input().split()):
    if dict_a[number]:
        cnt += 1

answer = (len_a - cnt) + (len_b - cnt)
print(answer)