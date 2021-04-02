import subprocess as sp
import os
import time
import json
import ssl
import argparse
from urllib import request
from minidatabase import Database

EXCEPT_FOLDER = [ 'solution', '.git', 'solutions', '.github', '__pycache__', 'markdown' ]
solution_list = dict()
changeLevel_list = list()
db = Database()

def getFolder(path, EXCEPT=[]):
    ret = [ folder for folder in os.listdir(f'{path}') \
            if os.path.isdir(f"{path}/{folder}") and folder not in EXCEPT ]
    return ret

def updateProblems():
    folders = getFolder('./', EXCEPT_FOLDER)
    problems = set()
    for folder in folders:
        lines = list()
        with open(f"{folder}/list.md", 'r') as f:
            lines = f.readlines()
            f.close()

        for line in lines:
            problemID = line.split(",")[-3]

            if problemID in problems:
                continue

            db.add(problemID)
            problems.add(problemID)


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

            problemName = ",".join(split_line[:-3][1:])

            # Validation

            problemINFO = db.getInfo(problemID)

            if problemName != problemINFO["name"]:
                print(" *** ERROR : WRONG PROBLEM NAME")
                print(f" TAG : {tag}")
                print(f"\"{problemName}\" -> \"{problemINFO['name']}\"")
                idx = 1
                for s_name in problemINFO["name"].split(","):
                    split_line[idx] = s_name
                    idx += 1
                update = True
            
            if levelUpdate:
                pre = split_line[-2]
                split_line[-2] = db.getInfo(problemID)["level"]
                if pre != split_line[-2]:
                    update = True
                    url       = f"https://www.acmicpc.net/problem/{problemID}"
                    changeLevel_list.append(f"[{problemID}]({url}) {pre} -> {split_line[-2]}\n")

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

def AutoUpdate():
    cmd = sp.check_output(['head -1 arrange.py'], shell=True).decode('utf8')
    cmd = cmd.split("#")[1]
    os.system(f"{cmd}")

def checkUpdate(folder, force_update=False):
    ret = sp.check_output(['git status'], shell=True).decode('utf8')
    print(ret)
    change = False
    for i in folder:
        if i in ret:
            change = True
            break

    if change or force_update:
        AutoUpdate()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser("Auto Update")
    arg = parser.add_argument

    arg('--all', dest='updateAll', action='store_true')
    parser.set_defaults(updateAll=False)

    arg('--solution', dest='updateSolution', action='store_true')
    parser.set_defaults(updateSolution=False)

    arg('--level', dest='updateLevel', action='store_true')
    parser.set_defaults(updateLevel=False)

    arg('--problem-update', dest='updateProblem', action='store_true')
    parser.set_defaults(updateProblem=False)

    arg('--push', dest='pushEvent', action='store_true')
    parser.set_defaults(pushEvent=False)

    args = parser.parse_args()

    if args.pushEvent:
        args.updateSolution = True
        args.updateProblem  = True

    if args.pushEvent or args.updateAll or args.updateSolution or updateProblem:
        os.system('python3 ./markdown/make_main_readme.py')

    if args.updateProblem:
        updateProblems()

    if args.updateAll or args.updateLevel:
        db.updateLevel()

    if args.updateAll or args.updateSolution:
        updateSolution()
        updateLevel = False
        if args.updateLevel or args.updateAll:
            updateLevel = True
        updateLIST(updateLevel)

        FOLDER = getFolder('./', EXCEPT_FOLDER)
        for i in FOLDER:
            run_script(i)

        # AutoUpdate()

    if len(changeLevel_list) > 0:
        changeLevel_list.append('#' * 30)
        with open("change_level.log", "a+") as f:
            f.writelines(changeLevel_list)
            f.close()

    db.saveDB()
    # checkUpdate(FOLDER, args.updateAll)
    AutoUpdate()
