from API import SolvedAPI
from make_table import Table
import json
import argparse
import os

config           = dict()
solution_list    = dict()
changeLevel_list = list()
api              = None
table            = None

def getFolder(path, EXCEPT=list()):
    return [ folder for folder in os.listdir(path) \
             if os.path.isdir(f"{path}/{folder}") and folder not in EXCEPT ]

# New Problem Update
def updateProblems():
    print("update start")
    table.run()
    print("update end")

# Solution Update
def updateSolution():
    rootFolder = "./solution"
    tagFolder  = getFolder(rootFolder) # in ./solution
    for tag in tagFolder:
        solution_list[tag] = set()
        problemPath        = f"{rootFolder}/{tag}"
        problems           = getFolder(problemPath)
        for problem in problems:
            solution_list[tag].add(problem)

# List.md 정리 (Solution Link)
def updateList():
    solutionRPATH = "./../solution"
    rootFolder    = "./"
    tagFolder     = config.get('tags')
    for tag in tagFolder:
        currentPath = f"{rootFolder}/{tag}"
        INFO = None

        with open(f"{currentPath}/list.md", 'r') as f:
            INFO = f.readlines()
            f.close()

        update = False
        NEWINFO = list()
        for line in INFO:
            split_line = line.split(",")
            problemId = split_line[-2]

            if tag in solution_list and problemId in solution_list[tag]:
                split_line[-1] = f"{solutionRPATH}/{tag}/{problemId}\n"
                update = True

            line = ",".join(split_line)
            NEWINFO.append(line)

        if update:
            with open(f"{currentPath}/list.md", 'w') as f:
                f.writelines(NEWINFO)
                f.close()

def updateStatus():
    os.system('python3 ./scripts/arrange.py > status.md')

def updateLevel():
    table.run(force = True)

if __name__=="__main__":

    # Read Config
    with open('./scripts/config.json', 'r') as f:
        config = json.load(f)
        f.close()

    api = SolvedAPI(config.get('API'))
    table = Table(api, config)

    parser = argparse.ArgumentParser('Auto Update')
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

    print("START")

    if args.pushEvent:
        args.updateSolution = True
        args.updateProblem  = True

    if args.pushEvent or args.updateAll or args.updateSolution:
        os.system('python3 ./scripts/make_main_readme.py')

    if args.updateAll or args.updateLevel:
        updateLevel()

    if args.updateAll or args.updateSolution:
        updateSolution()
        updateList()
    
    if args.updateProblem:
        updateProblems()

    updateStatus()
