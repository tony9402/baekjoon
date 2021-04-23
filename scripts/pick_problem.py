from API import SolvedAPI
import json
import subprocess as sp
import os
import datetime
import pytz

os.system('g++ -std=c++17 ./scripts/pick_problem.cpp -o ./scripts/pick.problem')

def reset():
    database = dict()
    with open('./scripts/database.json', 'r') as f:
        database = json.load(f)
        f.close()

    pick_data = list()
    for key, data in database.items():
        if 1 <= data.get('problemLevel') <= 15:
            line = f"{key}${data.get('problemLevel')}\n"
            pick_data.append(line)

    with open('./scripts/pick_data.in', 'w') as f:
        f.writelines(pick_data)
        f.close()

def pick():
    data = None
    with open('./scripts/pick_data.in', 'r') as f:
        data = f.readlines()
        f.close()

    if len(data) <= 30:
        reset()

    os.system('./scripts/pick.problem < ./scripts/pick_data.in > ./scripts/today_problem.out')
    with open("./scripts/today_problem.out", "r") as f:
        ret = [ _.strip() + '$' for _ in f.readlines() ]
        f.close()

    remain = list()
    picked = list()
    for v in ret:
        for idx, line in enumerate(data):
            if line.startswith(v):
                picked.append(line)
                del data[idx]
                break

    remain = data

    preData = list()
    with open('./picked.md', 'r') as f:
        preData = f.readlines()
        f.close()

    timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    saveline = [ f"## {timeformat.strftime('%Y/%m/%d')}\n" ]
    saveline.append('\n')
    saveline.append("| 난이도 | 번호 | 문제 이름 |\n")
    saveline.append("|:------:|:----:|:---------:|\n")
    for problem in picked:
        problemId, problemLevel = problem.strip().split('$')
        problemInfo = api.request(problemId)
        problemName = problemInfo.get('problemName')
        imageurl = f"<img height=\"25px\" width=\"25px\" src=\"https://static.solved.ac/tier_small/{problemLevel}.svg\"/>"
        line = f"| {imageurl} | [{problemId}](https://www.acmicpc.net/problem/{problemId}) | [{problemName}](https://www.acmicpc.net/problem/{problemId}) |\n"
        saveline.append(line)
    saveline.append('\n')
    saveline += preData

    with open('./picked.md', 'w') as f:
        f.writelines(saveline)
        f.close()

    with open('./scripts/pick_data.in', 'w') as f:
        f.writelines(remain)
        f.close()

if __name__ == "__main__":
    config = None
    with open('./scripts/config.json', 'r') as f:
        config = json.load(f)
        f.close()

    api = SolvedAPI(config.get("API"))
    pick()
