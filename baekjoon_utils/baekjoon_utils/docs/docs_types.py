from typing import Optional

from pydantic import BaseModel, Field

from baekjoon_utils.baekjoon_types import (
    ProblemType,
)

"""
각 Tag에서 문제를 list.md에 뽑아놓은 것들
"""
class ProblemListType(BaseModel):
    recommend: bool = Field(default=False)
    problemId: int = Field(...)
    solution_path: Optional[str] = Field(default=None)


class ProblemInfoType(ProblemListType, ProblemType):

    def __lt__(self, other):
        if self.recommend ^ other.recommend:
            return self.recommend

        if self.level != other.level:
            return self.level < other.level

        if self.averageTries != other.averageTries:
            return self.averageTries > other.averageTries

        return self.problemId < other.problemId


"""
Contributors 타입
"""
class ContributorType(BaseModel):
    id: int = Field(...)
    baekjoon_handle: str = Field(...)
    github_handle: Optional[str] = Field(...)
    github_id: Optional[str] = Field(...)
    hidden_all: bool = Field(default=False)
    hidden_info: bool = Field(default=False)

    def __lt__(self, other):
        return self.id < other.id
