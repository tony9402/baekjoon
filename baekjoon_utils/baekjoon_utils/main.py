import os
import argparse
from glob import glob

from baekjoon_utils.daily.pick import TodayProblemPicker
from baekjoon_utils.docs.problem import ProblemByTag
from baekjoon_utils.core.solved_api import SolvedAPI
from baekjoon_utils.utils import get_today_date_kst_str


def get_option():
    parser = argparse.ArgumentParser('Baekjoon Auto Update')
    arg = parser.add_argument

    arg('--update', dest='updateProblem', action='store_true')
    parser.set_defaults(updateProblem=False)

    arg('--pick', dest='pickProblem', action='store_true')
    parser.set_defaults(pickProblem=False)

    args = parser.parse_args()

    res = 0
    if args.updateProblem:
        res |= 2

    if args.pickProblem:
        res |= 1

    return res


def main():
    option = get_option()

    api = SolvedAPI()
    if option & 2:
        api.update_all()
        tags = glob("algorithms/*")
        for tag_path in tags:
            tag = os.path.basename(tag_path)
            p = ProblemByTag(tag)
            with open(os.path.join(tag_path, "header.md"), "r") as f:
                header = f.read()
                f.close()

            with open(os.path.join(tag_path, "README.md"), "w") as f:
                f.write(header + "\n\n")
                f.write(p.make_table())
                f.close()

            with open("update_log.md", "w") as f:
                f.write(get_today_date_kst_str())
                f.close()

    if option & 1:
        picker = TodayProblemPicker()
        today_problems = picker.pick_today_problem()
        table = picker.make_table(today_problems)

        with open("picked_legacy.md", "r") as f:
            before_problems = f.read()
            f.close()

        with open("picked_legacy.md", "w") as f:
            f.write(table + "\n\n")
            f.write(before_problems)
            f.close()

        with open("picked.md", "w") as f:
            f.write(table)
            f.close()


if __name__ == "__main__":
    main()
