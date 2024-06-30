
import json
from typing import Tuple, List, Optional
import random
from random import choice
from collections import defaultdict

from baekjoon_utils.utils import get_today_date, get_today_random_seed, get_today_date_kst_str, get_problem_url
from baekjoon_utils.core.database import Database
from baekjoon_utils.baekjoon_types import ProblemType


class TodayProblemPicker:
    before_days = 20
    max_level = [8, 12, 15, 18]
    choose_count = [1, 2, 1, 1]

    def __init__(self, path: str = "./scripts/picked.json"):
        with open(path, 'r') as f:
            self.data = json.load(f)
            f.close()

        self.database = Database()

    def save(self, path: str = "./scripts/picked.json"):
        with open(path, 'w') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            f.close()

    def pick_today_problem(self, date: Tuple[int, int, int] = get_today_date()) -> List[ProblemType]:
        seed = get_today_random_seed(date)
        random.seed(seed)

        dates = sorted(self.data.keys())[-self.before_days:]
        count = defaultdict(int)
        for key in dates:
            for problem_id in self.data[key]:
                count[problem_id] += 1

        sections = defaultdict(list)
        for problem_id in self.database.keys():
            problem = self.database[problem_id]
            if problem.level == 0 or problem.level > self.max_level[-1]:
                continue
            start_level = 1
            for section_idx, max_level in enumerate(self.max_level):
                if start_level <= problem.level <= max_level:
                    weight = int(self.before_days - count[problem.problemId] * 1.7)
                    weight = max(0, weight)
                    if weight:
                        sections[section_idx].extend([problem.problemId for _ in range(weight)])
                start_level = max_level + 1

        picked_problem = set()
        result = []
        for section in range(len(self.max_level)):
            chose = 0
            while chose < self.choose_count[section]:
                problem_id = choice(sections[section])
                if problem_id in picked_problem:
                    continue
                picked_problem.add(problem_id)
                result.append(self.database[str(problem_id)])
                chose += 1

        y, m, d = date
        picked_date = f"{y:04d}/{m:02d}/{d:02d}"
        new_data = {}
        new_data[picked_date] = [str(x.problemId) for x in result]
        new_data.update(self.data)
        self.data = new_data

        return result

    def make_table(self, problems: Optional[List[ProblemType]] = None) -> str:
        if problems is None:
            problems = self.pick_today_problem()

        date = get_today_date_kst_str()

        res = []
        res.append(f"## {date}\n")
        res.append(f"| 번호 | 문제 이름 |")
        res.append(f"| :----: | :---------: |")
        for problem in problems:
            problem_url = get_problem_url(problem.problemId)
            res.append(f"| [{problem.problemId}]({problem_url}) | [{problem.titleKo}]({problem_url}) |")
        return "\n".join(res)


if __name__ == "__main__":
    t = TodayProblemPicker()
    print(t.make_table())
