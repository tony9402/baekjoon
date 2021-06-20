# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/d59f549a75a84dd28c01a0f9c08eb169

import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    
    password = input()
    
    if password == 'END':
        break
    else:
        print(password[::-1])