import subprocess as sp
import os
import time


"""
정보 업데이트 (목표 : 거의 자동화)
 1. README 업데이트
 2. Solution Link 업데이트
 3. list.md 업데이트
"""

EXCEPT_FOLDER = [ 'solution', '.git', 'solutions' ]
solution_list = dict()

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


# list.md 정리
def updateLIST():
    # ./../solution/implementation/1212
    solutionRPATH = "./../solution"
    currentFolder = "./"
    tagFolder = getFolder(currentFolder, EXCEPT_FOLDER)
    for tag in tagFolder:
        if tag not in solution_list:
            continue
        currentPath = f"{currentFolder}/{tag}"
        INFO = None
        with open(f"{currentPath}/list.md", "r") as f:
            INFO = f.readlines()
            f.close()

        update = False
        NEWINFO = list()
        for line in INFO:
            split_line = line.split(",")
            if split_line[0] == '':
                NEWINFO.append(line)
                continue

            problemID = split_line[-3]
            if problemID in solution_list[tag]:
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

updateSolution()
updateLIST()
exit(0)

def run_script(path):
    if not os.path.isfile('make_table.py'):
        print("Not Found make_table.py")
        exit(0)
    ret = os.system(f"cat {path}/header.md > {path}/README.md")
    if ret != 0:
        exit(0) # 
    ret = os.system(f"python3 make_table.py < {path}/list.md >> {path}/README.md")
    if ret != 0: 
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

if __name__ == "__main__":
    updateSolution()
    updateLIST()

    FOLDER = getFolder('./', EXCEPT_FOLDER)
    for i in FOLDER:
        run_script(i)

    checkUpdate(FOLDER)
