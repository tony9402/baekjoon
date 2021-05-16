# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/2eb814a8afac4ceab99cbb89db78a2c6
import sys
import heapq
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

for T in range(int(input())):
    max_q = []
    min_q = []
    total_ele_cnt = 0
    elements_cnt = defaultdict(int)
    for _ in range(int(input())):
        operator, number = input().split()
        if operator == 'I':
            number = int(number)
            heapq.heappush(max_q, -number)
            heapq.heappush(min_q, number)
            elements_cnt[number] += 1
            total_ele_cnt += 1
        else:
            if total_ele_cnt > 0:
                if number == '1':
                    while True:
                        del_num = -heapq.heappop(max_q)
                        if elements_cnt[del_num] != 0:
                            elements_cnt[del_num] -= 1
                            break
                else:
                    while True:
                        del_num = heapq.heappop(min_q)
                        if elements_cnt[del_num] != 0:
                            elements_cnt[del_num] -= 1
                            break
                total_ele_cnt -= 1
    if total_ele_cnt:
        while True:
            max_v = -heapq.heappop(max_q)
            if elements_cnt[max_v] != 0:
                break
        while True:
            min_v = heapq.heappop(min_q)
            if elements_cnt[min_v] != 0:
                break
        print(max_v, min_v)
    else:
        print('EMPTY')