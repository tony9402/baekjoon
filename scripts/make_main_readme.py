import os
import subprocess as sp

seq = [ "header.md", "codingtest_info.md", "workbook_header.md", "workbook.md", "workbook_footer.md", "contributors.md", "updatelog.md", "TODO.md", "footer.md" ]

EXCEPT_FOLDER = [ 'solution', '.git', 'solutions', '.github', '__pycache__', 'markdown', "scripts" ]

def getCount(folder):
    lines = list()
    with open(f'./{folder}/list.md', 'r') as f:
        lines = f.readlines()
        f.close()

    total = 0
    cnt   = 0
    for line in lines:
        S = line.split(",")[0]
        total += 1
        if S != '':
            cnt += 1

    return cnt, total

def make_table(file="./markdown/list.md"):
    lines = list()
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()

    ret  = "| 순번 | Tag                          | 태그                | 문제집    | 추천 문제 수 | 총 문제 수 |  상태             |\n"
    ret += "| :--: | :--------------------------: | :-----------------: | :------:  | :---------:  | :------: |:---------------:|\n"
    for idx, line in enumerate(lines):
        folder, tag_en, tag_kr, status = line.strip().split(',')
        rec_cnt, total = getCount(folder)
        curLine = f"| {idx:02d} | {tag_en} | {tag_kr} | [바로가기](./{folder}) | {rec_cnt:02d} | {total:02d} | ![status][{status}] |\n"
        ret += curLine

    ret += ' \n \n\n '

    with open('./markdown/workbook.md', 'w') as f:
        f.write(ret)
        f.close()

def assemble():
    with open('./README.md', 'w') as f:
        f.close()

    for md in seq:
        os.system(f"cat ./markdown/{md} >> ./README.md")

def make_contributors():
    os.system('python3 ./scripts/make_contributor.py')

if __name__=="__main__":
    make_contributors()
    make_table()
    assemble()
