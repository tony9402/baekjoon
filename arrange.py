# python3 arrange.py > status.md

import subprocess as sp
import os
import time

EXCEPT_FOLDER = [ 'solution', '.git', 'solutions' ]

def getProblem(Dir):
    ret = list()
    with open(f"{Dir}/list.md", 'r') as f:
        ret = f.readlines()
        f.close()
    return ret

def Assemble(*args):
    problems = set()
    for i in args:
        for problem in i:
            problemID = problem.split(',')[-3]
            problems.add(problemID)
    return problems

def Status(tags, *args): # Problems, Folders
    for idx, problems in enumerate(args):
        print(f"| {idx:02d} |  [{tags[idx]}](./../../tree/main/{tags[idx]}) | ", end='')
        totalProblem = 0 # Only ✔️
        hasEditoral = 0
        for problem in problems:
            info = problem.split(',')

            rec  = info[0].strip()
            link = info[-1].strip()
            if not link == '':
                hasEditoral += 1
            if not rec == '':
                totalProblem += 1

        if totalProblem == 0: # Except 0 / 0
            totalProblem = 1  # Make 0 / 1

        # https://img.shields.io/badge/-{1}-31AE0F
        # DFFD26 0885CC
        percent = hasEditoral / totalProblem * 100.
        color   = "DFFD26"

        if percent == 100.0:
            color = "0885CC"
        elif percent != 0.0:
            color = "31AE0F"

        print(f"![status](https://img.shields.io/badge/-{percent:.2f}%25-{color}) |  ")

def getTier(Str):
    if len(Str) == 2: # Ex p2, P2...
        return Str.upper()
    else: # Gold5...
        return Str[0].upper() + Str[-1]

def getRecommend(*args):
    ret = list() # Not Set, Get Problem Info (ProblemID, Problem Name, Tier)
    for i in args:
        for problem in i:
            info = problem.split(",")
            rec = info[0].strip()
            if not rec == '':
                ret.append((info[-3], ','.join(info[:-3][1:]), getTier(info[-2])))
    return ret

# Clean Code 생각 X
# TODO 
def calPercentageOfRec(*args):
    total = 0
    hasSolution = 0

    for i in args:
        for problem in i: 
            info = problem.split(",")
            rec  = info[0].strip()
            link = info[-1].strip()
            if rec == '':
                continue
            total += 1
            
            if not link == '':
                hasSolution += 1
    return float(hasSolution) / total


# Get Folders
Folders = sorted([ _ for _ in os.listdir('./') if os.path.isdir(_) and not _ in EXCEPT_FOLDER and not _.startswith('.') ])
Problems = [ getProblem(_) for _ in Folders ]
TotalProblem = Assemble(*Problems)

# getStatus(Folders, *Problems)
Recommend_List = getRecommend(*Problems)

print("""# Status

간단하게 파이썬으로 진행사항 및 문제 수를 알아보기 위해 만들어 보았습니다.


[메인으로 돌아가기](https://github.com/tony9402/baekjoon)


""")

print(f"총 문제 수 : {len(TotalProblem)}  ")
print(f"총 추천 문제 수 : {len(Recommend_List)} ({len(Recommend_List) / len(TotalProblem) * 100. :.2f}%)  ")
print(f"알고리즘 Tag 개수 : {len(Folders)}  ")
print("\n") # lnln

print("<hr>")
print(f"각 알고리즘 Tag 진행 사항 <b>(Tag는 사전순)</b> {calPercentageOfRec(*Problems):.2f}% <br><br>\n")

# Make Table (Markdown)

print("| Index | Tag(Folder Name) | Solution 진행도 |")
print("| :--:  | :--------------- | :------------:  |")
Status(Folders, *Problems)

now = time.localtime()
print(f"\n\n**실행한 날짜(log) : {now.tm_year:04d}/{now.tm_mon:02d}/{now.tm_mday:02d}**")
