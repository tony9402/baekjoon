import os
from typing import Dict

from baekjoon_utils.core.database import (
    Database,
)
from baekjoon_utils.utils import (
    get_problem_url,
    make_href,
    make_level_image,
)
from baekjoon_utils.docs.docs_types import (
    ProblemListType,
    ProblemInfoType,
)


class ProblemByTag:
    def __init__(self, algorithm_tag: str):
        path = f"algorithms/{algorithm_tag}"
        database = Database()

        with open(os.path.join(path, "list.md"), "r") as f:
            problems = [x.strip().split(',') for x in f.readlines() if x.strip()]
            f.close()

        problems = [
            ProblemListType(recommend=line[0] == '1', problemId=int(line[1]), solution_path=line[2])
            for line in problems
        ]
        self.problems = []

        self.count_of_problem = {
            "recommend": 0,
            "total": 0,
        }
        for problem in problems:
            if problem.recommend:
                self.count_of_problem["recommend"] += 1
            self.count_of_problem["total"] += 1
            problem_id = f"{problem.problemId}"
            problem_data = database[problem_id].model_dump()
            problem_data.update(
                problem.model_dump(),
            )
            self.problems.append(
                ProblemInfoType.model_validate(problem_data)
            )

        self.problems.sort()

    def make_table(self) -> str:
        headers = ["순번", "추천 문제", "문제 번호", "문제 이름", "난이도", "풀이 링크"]
        markdown_table = []

        markdown_table.append("|" + "|".join(headers) + "|")
        markdown_table.append("|" + "|".join([":--:"] * len(headers)) + "|")

        for idx, problem in enumerate(self.problems):
            problem_url = get_problem_url(problem.problemId)
            level_badge_url = make_level_image(problem.level)
            line = [
                f"{idx:03d}",  # 순번
                ":heavy_check_mark:" if problem.recommend else "",  # 추천 문제
                make_href(problem_url, problem.problemId),  # 문제 번호
                make_href(problem_url, problem.titleKo),  # 문제 이름
                level_badge_url,  # 난이도
                make_href(problem.solution_path, "바로 가기") if problem.solution_path else "",
            ]
            markdown_table.append("|" + "|".join(line) + "|")

        return "\n".join(markdown_table)

    def get_info(self) -> Dict[str, int]:
        return self.count_of_problem
