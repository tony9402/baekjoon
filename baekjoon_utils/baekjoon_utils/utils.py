import ssl
import json
import random
from datetime import datetime, timezone, UTC, timedelta
from typing import Union, Tuple
from urllib import request


def get_problem_url(problem_id: Union[int, str]) -> str:
    return f"https://www.acmicpc.net/problem/{problem_id}"


def make_href(url: str, title: str = "", target_blank: bool = True) -> str:
    if target_blank:
        res = f"<a href=\"{url}\" target=\"_blank\">{title}</a>"
    else:
        res = f"<a href=\"{url}\">{title}</a>"
    return res


def make_level_image(level: int) -> str:
    return f"<img height=\"25px\" width=\"25px\" src=\"https://static.solved.ac/tier_small/{level}.svg\"/>"


def level_to_str(level: int) -> str:
    _prefix = "BSGPDR"
    level -= 1
    prefix_str = _prefix[level // 5]
    level = 5 - level % 5
    return f"{prefix_str}{level}"


def get_api_result(url, headers):
    ssl_context = ssl._create_unverified_context()

    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req, context=ssl_context)

    return json.loads(response.read().decode("utf-8"))


def get_today_date():
    utctime = datetime.now(UTC)
    ksttime = utctime.astimezone(timezone(timedelta(hours=9)))
    return ksttime.year, ksttime.month, ksttime.day


def get_today_date_kst_str():
    y, m, d = get_today_date()
    return f"{y:04d}/{m:02d}/{d:02d}"


def get_today_random_seed(date: Tuple[int, int, int] = get_today_date()):
    range_max = [1073741823, 32768, 128]

    seed = 0
    for a, b in zip(date, range_max):
        random.seed(a)
        seed += random.randint(1, b)
    return seed
