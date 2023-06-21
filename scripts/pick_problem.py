import datetime
import random
import json
import urllib.request as request
from utils import Date, Communication


def get_today_date():
    year, month, day = Date.get_today_date()
    timeformat = f"{year:04d}/{month:02d}/{day:02d}"
    return timeformat


def make_table(data: dict, save_file: str) -> None:
    database = Communication.get_database()

    lines = []
    for date, problems in data.items():
        lines.append(f"## {date} \n\n")
        lines.append("| 번호 | 문제 이름 |\n")
        lines.append("|:----:|:---------:|\n")
        for problem_id in problems:
            problemName = database[problem_id]['problemName']
            link = f"https://www.acmicpc.net/problem/{problem_id}"
            line = f"| [{problem_id}]({link}) | [{problemName}]({link}) |\n"
            lines.append(line)
        lines.append('\n')

    with open(save_file, 'w') as f:
        f.writelines(lines)
        f.close()


def pick():
    picked_json = dict()
    with open('./scripts/picked.json', 'r') as f:
        picked_json = json.load(f)
        f.close()

    timeformat = get_today_date()

    today_problems: list = Communication.get_today_problem()
    new_data = {}
    new_data[timeformat] = today_problems
    new_data.update(picked_json)

    with open('./scripts/picked.json', 'w') as f:
        f.write(json.dumps(new_data, indent=4, ensure_ascii=False))
        f.close()

    return new_data


def main():
    data = pick()
    today = get_today_date()
    make_table({today : data[today]}, './picked.md')
    make_table(data, './picked_legacy.md')


if __name__ == "__main__":
    main()
