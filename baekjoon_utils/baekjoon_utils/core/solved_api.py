from urllib import parse
from typing import List, Optional, Union, Dict

from tqdm.auto import tqdm

from baekjoon_utils.core.database import Database
from baekjoon_utils.baekjoon_types import ProblemType
from baekjoon_utils.utils import get_api_result


def get_solved_headers():
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
        "x-solvedac-language": "ko",
    }
    return headers


def get_url(
    scheme:str="https",
    netloc: str="solved.ac",
    base_path: str="/api/v3",
    path: str="",
    params: str="",
    query: Union[str, Dict[str, str]]="",
    fragment: str=""
) -> str:
    if isinstance(query, dict):
        queries = [f"{k}={v}" for k, v in query.items()]
        query = "&".join(queries)

    config = {
        "scheme": scheme,
        "netloc": netloc,
        "path": "/".join([base_path.rstrip('/'), path.lstrip('/')]),
        "params": params,
        "query": query,
        "fragment": fragment,
    }

    return parse.ParseResult(**config).geturl()


class SolvedAPI:
    def __init__(self, config=None):
        self.config = config
        self.database = Database()

    def update_all(self, problem_ids: Optional[List[str]] = None):
        if problem_ids is None:
            problem_ids = self.database.keys()

        batch_size = 100
        total_iteraion = (len(problem_ids) + batch_size - 1) // batch_size
        for batch_start_index in tqdm(range(0, len(problem_ids), batch_size), total=total_iteraion):
            batch = problem_ids[batch_start_index:batch_start_index+batch_size]
            results = self.get_problems(batch)
            for result in results:
                problemId = f"{result.problemId}"
                self.database[problemId] = result

    def get_problems(self, problem_ids: List[str]):
        if len(problem_ids) > 100:
            raise Exception("Too Many Problems. Must be <= 100")

        url = get_url(
            path="problem/lookup",
            query={
                "problemIds": ",".join(problem_ids),
            },
        )
        headers = get_solved_headers()
        res_problems = get_api_result(url=url, headers=headers)
        return [
            ProblemType.model_validate(res)
            for res in res_problems
        ]

    def get_problem(self, problem_id: str):
        return self.get_problems(problem_ids=[problem_id])[0]

