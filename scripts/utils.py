import datetime
import random
import json
import urllib.request as request


class Date:
    @staticmethod
    def get_today_date():
        utctime = datetime.datetime.utcnow()
        ksttime = utctime.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
        return ksttime.year, ksttime.month, ksttime.day

    @classmethod
    def get_today_random_seed(cls):
        year, month, day = cls.get_today_date()
        random.seed(year)
        first_random_value = random.randint(1, 1073741823)
        random.seed(month)
        second_random_value = random.randint(1, 32768)
        random.seed(day)
        third_random_value = random.randint(1, 128)

        random_seed = first_random_value + second_random_value + third_random_value
        return random_seed


class Communication:
    __URL = {
        "database": "https://raw.githubusercontent.com/tony9402/baekjoon/main/scripts/database.json",
        "picked_problem": "https://raw.githubusercontent.com/tony9402/baekjoon/main/scripts/picked.json",
    }
    __hyperparameter = {
        "before_days": 20,
        "n_section": 4,
        "max_level": [8, 12, 15, 18], # [S3, G4, G1, P3]
        "choose_count": [1, 2, 1, 1],
    }

    @staticmethod
    def get_json(url):
        text = request.urlopen(url).read()
        json_data = json.loads(text)
        return json_data

    @classmethod
    def get_database(cls):
        return cls.get_json(cls.__URL['database'])

    @classmethod
    def get_picked_problem(cls):
        return cls.get_json(cls.__URL['picked_problem'])

    @classmethod
    def get_today_problem(cls):
        today_problems = []

        seed = Date.get_today_random_seed()
        random.seed(seed)

        all_problem = cls.get_database()
        picked_problem = cls.get_picked_problem()

        param = cls.__hyperparameter
        dates = sorted(picked_problem.keys(), reverse=True)[:param['before_days']]
        used_problem = set()
        for date in dates:
            used_problem.update(picked_problem[date])

        used_problem = [[] for section in range(param['n_section'])]
        splitted_problem = [[] for section in range(param['n_section'])]
        for problem_id, problem_info in all_problem.items():
            problemlevel = int(problem_info['problemLevel'])
            if not 1 <= problemlevel <= 18:
                continue

            section = 0
            while section < len(param['max_level']) and problemlevel > param['max_level'][section]:
                section += 1

            assert section < param['n_section']

            if problem_id in used_problem: 
                used_problem[section].append(problem_id)
            else:
                splitted_problem[section].append(problem_id)

        for section, problems in enumerate(splitted_problem):
            if len(problems) < param['choose_count'][section]:
                problems.extend(used_problem[section])
            problems = random.sample(problems, k=param['choose_count'][section])
            today_problems.extend(problems)

        return today_problems

