import json
import os

data = dict()
contributors = list()

with open('./markdown/contributor.json', 'r') as f:
    data = json.load(f)
    contributors = data.get('id')
    f.close()

LIST = list()
LN   = "\n"

# Header
LIST.append("## Contributors")
LIST.append(LN)

LIST.append("<table>")

idx = 0
columns = 5
SP  = "    "
N   = len(contributors)

while idx < N:
    cur = contributors[idx:idx + columns]

    # TOP
    LIST.append(f"{SP}<tr height=\"140px\">")
    for ID in cur:
        GITHUBID = data[ID]["githubid"]
        LIST.append(f"{SP}{SP}<td align=\"center\" width=\"130px\">")
        LIST.append(f"{SP}{SP}{SP}<a href=\"https://github.com/{ID}\"><img height=\"100px\" width=\"100px\" src=\"https://avatars.githubusercontent.com/u/{GITHUBID}?v=4\"/></a>")
        LIST.append(f"{SP}{SP}{SP}<br />")
        LIST.append(f"{SP}{SP}{SP}<a href=\"https://github.com/{ID}\">{ID}</a>")
        LIST.append(f"{SP}{SP}</td>")
    LIST.append(f"{SP}</tr>")

    # BOTTOM
    LIST.append(f"{SP}<tr height=\"50px\">")
    for ID in cur:
        baekjoon = data[ID]["baekjoon"]
        LIST.append(f"{SP}{SP}<td align=\"center\">")
        if baekjoon == "$":
            LIST.append(f"{SP}{SP}{SP}<b>PRIVATE</b>")
        else:
            LIST.append(f"{SP}{SP}{SP}<img src=\"http://mazassumnida.wtf/api/mini/generate_badge?boj={baekjoon}\" />")
            LIST.append(f"{SP}{SP}{SP}<br />")
            LIST.append(f"{SP}{SP}{SP}<a href=\"https://www.acmicpc.net/user/{baekjoon}\">Baekjoon</a>")
            LIST.append(f"{SP}{SP}{SP}<br />")
            LIST.append(f"{SP}{SP}{SP}<a href=\"https://solved.ac/profile/{baekjoon}\">solved.ac</a>")
        LIST.append(f"{SP}{SP}</td>")
    LIST.append(f"{SP}</tr>")
    idx = idx + columns

LIST.append("</table>")
LIST.append("\n")

LIST = [ f"{_}\n" for _ in LIST ]

with open('./markdown/contributors.md', 'w') as f:
    f.writelines(LIST)
    f.close()
