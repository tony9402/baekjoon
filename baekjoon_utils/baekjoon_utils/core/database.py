import json
import atexit
from typing import Optional, List

from baekjoon_utils.baekjoon_types import (
    ProblemType,
    DatabaseType,
)


class DatabaseModule:
    def __init__(self, path: str = "scripts/database.json"):
        self.db = None
        with open(path, 'r') as f:
            self.db = DatabaseType(problems=json.load(f))
            f.close()

        atexit.register(self.save)

    def __getitem__(self, problem_id: str):
        return self.db.problems[problem_id]

    def __setitem__(self, problem_id: str, problem_info: ProblemType):
        self.db.problems[problem_id] = problem_info

    def keys(self) -> List[str]:
        return list(self.db.problems.keys())

    def save(self, path: str = "scripts/database.json"):
        if self.db is not None:
            with open(path, "w") as f:
                json.dump(self.db.model_dump()["problems"], f, indent=4, ensure_ascii=False)
                f.close()


class Database:
    instance = None

    def __new__(cls, path: Optional[str] = None) -> DatabaseModule:
        if cls.instance is None:
            if path is None:
                cls.instance = DatabaseModule()
            else:
                cls.instance = DatabaseModule(path)
        return cls.instance

