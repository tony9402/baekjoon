from API import SolvedAPI
import json
import subprocess as sp
import os
import datetime
import pytz

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

    return pick_data

def update():
    data = None
    with open('./scripts/pick_data.in', 'r') as f:
        data = f.readlines()
        f.close()

    if len(data) <= 30:
        data = reset()

    problem_database = None
    with open('./scripts/database.json', 'r') as f:
        problem_database = json.load(f)
        f.close()

    newdata = list()
    for line in data:
        problemId, problemLevel = line.split('$')
        problemInfo = api.request(problemId)
        problemLevel = problemInfo["problemLevel"]
        newdata.append(f"{problemId}${problemLevel}\n")

    with open('./scripts/pick_data.in', 'w') as f:
        f.writelines(newdata)
        f.close()

def make_table():
    data = dict()
    with open('./scripts/picked.json', 'r') as f:
        data = json.load(f)
        f.close()

    saveline = []
    keys = data.keys()
    for key in keys:
        saveline.append(f"## {key} \n")
        saveline.append('\n')
        saveline.append("| 난이도 | 번호 | 문제 이름 |\n")
        saveline.append("|:------:|:----:|:---------:|\n")
        for problem in data[key]:
            problemInfo = api.request(problem)
            problemName = problemInfo.get('problemName')
            problemLevel = problemInfo.get('problemLevel')
            imageurl = f"<img height=\"25px\" width=\"25px\" src=\"https://static.solved.ac/tier_small/{problemLevel}.svg\"/>"
            line = f"| {imageurl} | [{problem}](https://www.acmicpc.net/problem/{problem}) | [{problemName}](https://www.acmicpc.net/problem/{problem}) |\n"
            saveline.append(line)

        saveline.append('\n')

    with open('./picked.md', 'w') as f:
        f.writelines(saveline)
        f.close()

def pick():
    os.system('g++ -std=c++17 ./scripts/pick_problem.cpp -o ./scripts/pick.problem')

    data = None
    with open('./scripts/pick_data.in', 'r') as f:
        data = f.readlines()
        f.close()

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

    picked_json = dict()
    with open('./scripts/picked.json', 'r') as f:
        picked_json = json.load(f)
        f.close()

    timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    timeformat = f"{timeformat.strftime('%Y/%m/%d')}"
    new_data = dict()
    new_data[timeformat] = list()
    for problem in picked:
        problemId, problemLevel = problem.strip().split('$')
        new_data[timeformat].append(problemId)

    new_data.update(picked_json)

    with open('./scripts/picked.json', 'w') as f:
        f.write(json.dumps(new_data, indent=4, ensure_ascii=False))
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
    
    update()
    pick()
    make_table()
