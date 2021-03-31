import subprocess as sp
import os
import time
import json
import ssl
import argparse
from urllib import request

EXCEPT_FOLDER = [ 'solution', '.git', 'solutions', '.github' ]
solution_list = dict()
changeLevel_list = list()

def getFolder(path, EXCEPT=[]):
    ret = [ folder for folder in os.listdir(f'{path}') \
            if os.path.isdir(f"{path}/{folder}") and folder not in EXCEPT ]
    return ret

# Solution 정보
def updateSolution():
    currentFolder = "./solution"
    tagFolder = getFolder(currentFolder)
    for tag in tagFolder:
        solution_list[tag] = set()
        problemPath = "/".join([currentFolder, tag])
        problems    = getFolder(problemPath)
        for problem in problems:
            solution_list[tag].add(problem)

def itol(level): ## Only Bronze ~ Platinum in my workbook
    NAME  = [ 'B', 'S', 'G', 'P', 'D' ]
    NUMB  = [   1,   2,   3,   4,   5 ]
    LEFT  = NAME[ (level - 1) // 5 ]
    RIGHT = NUMB[ 4 - (level - 1) % 5 ]
    return f"{LEFT}{RIGHT}"

def getLevel(problemID):
    ssl_context = ssl._create_unverified_context()
    url   = f"https://api.solved.ac/v2/problems/show.json?id={problemID}"
    res   = request.urlopen(request.Request(url), context = ssl_context)
    JSON  = json.loads(res.read().decode('UTF-8'))
    LEVEL = JSON["result"]["problems"][0]["level"]
    return itol(LEVEL)

# list.md 정리
def updateLIST(levelUpdate=False):
    solutionRPATH = "./../solution"
    currentFolder = "./"
    tagFolder = getFolder(currentFolder, EXCEPT_FOLDER)
    for tag in tagFolder:
        currentPath = f"{currentFolder}/{tag}"
        INFO = None
        with open(f"{currentPath}/list.md", "r") as f:
            INFO = f.readlines()
            f.close()

        update = False
        NEWINFO = list()
        for line in INFO:
            split_line = line.split(",")
            problemID = split_line[-3]
            
            if levelUpdate:
                pre = split_line[-2]
                split_line[-2] = getLevel(problemID)
                if pre != split_line[-2]:
                    update = True
                    url       = f"https://www.acmicpc.net/problem/{problemID}"
                    changeLevel_list.append(f"[{problemID}]({url}) {pre_rate} -> {cur_rate}\n")

            if split_line[0] == '':
                line = ",".join(split_line)
                NEWINFO.append(line)
                continue

            if tag in solution_list and problemID in solution_list[tag]:
                split_line[-1] = f"{solutionRPATH}/{tag}/{problemID}\n"
                update = True
            else:
                split_line[-1] = "\n"

            line = ",".join(split_line)
            NEWINFO.append(line)
        
        if update:
            with open(f"{currentPath}/list.md", "w") as f:
                f.writelines(NEWINFO)
                f.close()

def run_script(path):
    if not os.path.isfile('make_table.py'):
        print("Not Found make_table.py")
        exit(0)
    ret = os.system(f"cat {path}/header.md > {path}/README.md")
    if ret != 0:
        print("ERROR")
        exit(0) # 
    ret = os.system(f"python3 make_table.py < {path}/list.md >> {path}/README.md")
    if ret != 0: 
        print("ERROR")
        exit(0) # 

def checkUpdate(folder):
    ret = sp.check_output(['git status'], shell=True).decode('utf8')
    change = False
    for i in folder:
        if i in ret:
            change = True
            break

    if change:
        cmd = sp.check_output(['head -1 arrange.py'], shell=True).decode('utf8')
        cmd = cmd.split("#")[1]
        os.system(f"{cmd}")

def AutoUpdate():
    cmd = sp.check_output(['head -1 arrange.py'], shell=True).decode('utf8')
    cmd = cmd.split("#")[1]
    os.system(f"{cmd}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser("Auto Update")
    arg = parser.add_argument

    arg('--all', dest='updateAll', action='store_true')
    parser.set_defaults(updateAll=False)

    arg('--solution', dest='updateSolution', action='store_true')
    parser.set_defaults(updateSolution=False)

    arg('--level', dest='updateLevel', action='store_true')
    parser.set_defaults(updateLevel=False)

    args = parser.parse_args()
    
    if args.updateAll or args.updateSolution:
        updateSolution()
        updateLevel = False
        if args.updateLevel or args.updateAll:
            updateLevel = True
        updateLIST(updateLevel)

        FOLDER = getFolder('./', EXCEPT_FOLDER)
        for i in FOLDER:
            run_script(i)

        # checkUpdate(FOLDER)
        AutoUpdate()

    if len(changeLevel_list) > 0:
        changeLevel_list.append('#' * 30)
        with open("change_level.log", "a+") as f:
            f.writelines(changeLevel_list)
            f.close()
