# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/a2586b306e3340caa3740e5953662eeb
import sys
def input():
    return sys.stdin.readline().rstrip()

def isBig():
    if start[0] < end[0]:
        return 1
    elif start[0] == end[0]:
        if start[1] < end[1]:
            return 1
        elif start[1] == end[1]:
            if start[2] < end[2]:
                return 1
            elif start[2] == end[2]:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
            
start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
total = start[0] * 3600 + start[1] * 60 + start[2]
total2 = end[0] * 3600 + end[1] * 60 + end[2]
if isBig() == 1:
    ans = total2 - total
    hour, minute, second = str(ans // 3600), str(ans % 3600 // 60), str(ans % 60)
    hour = '0' * (2-len(hour)) + hour
    minute = '0' * (2-len(minute)) + minute
    second = '0' * (2-len(second)) + second
    print(f"%s:%s:%s" % (hour, minute, second))
elif isBig() == 0:
    print('24:00:00')
else:
    ans = total2 - total + 3600 * 24
    hour, minute, second = str(ans // 3600), str(ans % 3600 // 60), str(ans % 60)
    hour = '0' * (2-len(hour)) + hour
    minute = '0' * (2-len(minute)) + minute
    second = '0' * (2-len(second)) + second
    print(f"%s:%s:%s" % (hour, minute, second))