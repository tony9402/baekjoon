import os
import sys
import subprocess
import argparse
from bs4 import BeautifulSoup as bs
import requests

EXTENSION = [("py", "python", "main"), ("cpp", "cpp", "main"), ("java", "java", "Main")]

def run(command):
    ret = subprocess.check_output(command, shell=True).decode('utf8')
    return ret

def load_arg():
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('--pr_number', type=int, help="Pull Request Number")
    arg('--check_solution', action='store_true')
    parser.set_defaults(check_solution=False)
    return parser.parse_args()

def check_alreay_exist_solution(path):
    if os.path.exists(path):
        raise Exception("Alread Exists Solution")

    print("It is a new Solution!!")

def get_pr_file(pr_number):
    run(f"git fetch origin +refs/pull/{pr_number}/merge")
    files = run(f"git --no-pager diff --name-only FETCH_HEAD $(git merge-base FETCH_HEAD main)")
    files = [file.strip() for file in files.split() if file.strip() != ""]

    if len(files) != 1:
        raise Exception("No 1 PR 1 Solution")

    return files[0]

def get_solution_language(path):
    filename, extension = path.split('/')[-1].split('.')
    for info in EXTENSION:
        if info[0] == extension:
            if filename == info[2]:
                print(f"Found {info[1]} Language")
                return info[1]
            else:
                raise Exception(f"Wrong File name {filename}")

    raise Exception(f"No Found {extension} Language")

def detect_tab(path):
    with open(path, 'r') as f:
        solution = f.readlines()
        f.close()

    for line in solution:
        if '\t' in line:
            raise Exception("Detected Tab in this solution")

    print("No Detect Tab")

def get_example(problem_id):
    url = f"https://www.acmicpc.net/problem/{problem_id}"
    req = requests.get(url)
    html = bs(req.text, 'html.parser')
    spj = True if html.find('span', 'problem-label-spj') else False

    if spj:
        print("Found Special Judge")

    examples = []

    try:
        sample_id = 1
        while True:
            sample_input = html.select(f'#sample-input-{sample_id}')[0].text
            sample_output = html.select(f'#sample-output-{sample_id}')[0].text
            examples.append((sample_input, sample_output))
            sample_id += 1
    except:
        pass
    return spj, examples

def compile_test(path):
    try:
        extension = get_solution_language(path)
        if extension == 'cpp':
            run(f"g++ -std=c++17 {path} -o Main")
        elif extension == 'java':
            run(f"javac {path} -d  .")
    except:
        raise RuntimeError("Compile Error")

    return extension

def judge_test(path):
    detect_tab(path)
    problem = path.split('/')[-2]
    spj, samples = get_example(problem)

    extension = compile_test(path)

    print(f"Found {len(samples)} examples in {problem} problem")

    for idx, (data_input, data_output) in enumerate(samples):
        with open("example.in", 'w') as f:
            f.write(data_input)
            f.close()

        try:
            if extension == 'cpp':
                result = run(f"./Main < example.in")
            elif extension == 'python':
                result = run(f"python3 {path} < example.in")
            elif extension == 'java':
                result = run(f"java Main < example.in")
        except:
            raise Exception("Runtime Error")

        if spj:
            continue

        result = [ line.strip() for line in result if line.strip() != '']
        data_output = [ line.strip() for line in data_output if line.strip() != '' ]

        if result != data_output:
            raise Exception("Wrong Solution")

        print(f"Example {idx + 1} Correct !")

    print(f"{problem} Judge Success")

if __name__ == "__main__":
    args = load_arg()
    
    if args.check_solution:
        file = get_pr_file(args.pr_number)
        lang = get_solution_language(file)
        with open("result", 'w') as f:
            f.write(lang)
            f.close()
    else:
        file = get_pr_file(args.pr_number)
        check_alreay_exist_solution(file)
        run(f"git checkout FETCH_HEAD")
        judge_test(file)
