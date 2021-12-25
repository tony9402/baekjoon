# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/16de6b69c0ca419a908289ee440a407a

import sys

def input():
    return sys.stdin.readline().rstrip()

def calculate_days_per_month():
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = [0]
    for month, day in month_days.items():
        days.append(days[month-1] + day)
    return days

month_days = calculate_days_per_month()

def change_str(_str):
    date, time, item, person = _str.split()
    _, month, day = map(int, date.split('-')) # 년도 필요없음
    hour, minute = map(int, time.split(':'))
    return person, item, (month_days[month-1] + day) * 24 * 60 + hour * 60 + minute

def solution(info, deadline_time, F):
    dic = {}
    people = {} # 벌금 낼 사람들
    for data in info:
        result = -1
        person, item, time = change_str(data)
        if person not in dic:
            dic[person] = {}
        if item in dic[person]:
            result = time - dic[person].pop(item)
        else:
            dic[person][item] = time
        if result > deadline_time:
            if person not in people:
                people[person] = 0
            people[person] += (result - deadline_time) * F
    if people:
        people = sorted(people.items(), key = lambda x: x[0])
        for person, pay in people:
            print('{} {}'.format(person, pay))
    else:
        print(-1)

N, L, F = input().split()
N, F = int(N), int(F)
day, time = L.split('/')
day = int(day)
hour, minute = map(int, time.split(':'))
deadline_time = day*24*60 + hour*60 + minute
info = []
for _ in range(N):
    _str = input()
    info.append(_str)

solution(info, deadline_time, F)
