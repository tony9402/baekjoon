# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/6aa21ec4df1e483a9982f216802d7bd3

import sys
def input():
    return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]
    people.sort()

    cnt = 0
    minimum = n+1
    for person in people:
        if person[1] < minimum:
            cnt += 1
            minimum = person[1]
    print(cnt)
