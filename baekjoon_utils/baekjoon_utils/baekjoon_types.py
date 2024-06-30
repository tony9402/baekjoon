from typing import List, Dict

from pydantic import BaseModel, Field


class ProblemTagNamesType(BaseModel):
    language: str = Field(default="")
    name: str = Field(default="")
    short: str = Field(default="")


class ProblemTagType(BaseModel):
    key: str = Field(default="")
    bojTagId: int = Field(default=-1)
    displayNames: List[ProblemTagNamesType] = Field(default_factory=list)


class ProblemType(BaseModel):
    problemId: int = Field(...)
    titleKo: str = Field(...)
    isSolvable: bool = Field(...)
    level: int = Field(default=0)
    averageTries: float = Field(default=0.0)
    tags: List[ProblemTagType] = Field(default_factory=list)


class DatabaseType(BaseModel):
    problems: Dict[str, ProblemType] = Field(default_factory=dict)

