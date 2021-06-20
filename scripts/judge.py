from glob import glob
import subprocess as sp
from bs4 import BeautifulSoup as bs
import requests
import os
import sys

path = sys.stdin.readline().strip().split(' ')[1]
language = path.split('.')[-1]
check_all = True

def printError():
    print("ERROR")

if language not in [ 'py', 'cpp', 'java' ]:
    check_all = False

if not check_all:
    printError()
    exit(0)

data = list()
with open(path, 'r') as f:
    data = f.readlines()

user_name = ''
link      = ''
HASH      = 0

for line in data:
    after_strip = line.strip()
    if "Authored by" in after_strip:
        user_name = after_strip.split(':')[-1].strip()
    if "Link" in after_strip:
        link      = after_strip.split(':')[-1].strip()
        HASH      = link.split('/')[-1]

if user_name == '' or link == '' or HASH == 0:
    check_all = False

if not check_all:
    printError()
    exit(0)

# check Link
url  = f"https://www.acmicpc.net/source/share/{HASH}"
req  = requests.get(url).text
html = bs(req, 'html.parser')
boj_user = html.select('body > div.wrapper > div.breadcrumbs > div > ul > li > a')[0].text
result   = html.select('body > div.wrapper > div.container.content > div > section > div:nth-child(3) > div > table > tbody > tr > td:nth-child(1) > span')[0].text
memory   = html.select('body > div.wrapper > div.container.content > div > section > div:nth-child(3) > div > table > tbody > tr > td:nth-child(2)')[0].text + " KB"
time     = html.select('body > div.wrapper > div.container.content > div > section > div:nth-child(3) > div > table > tbody > tr > td:nth-child(3)')[0].text + " ms"

if boj_user != user_name or result != "맞았습니다!!":
    check_all = False

if not check_all:
    printError()
    exit(0)

problemID = path.split('/')[-2]
tag       = path.split('/')[-3]
print("SUCCESS")
print(f"솔루션 경로 : {path}")
print(f"BOJ USER : {boj_user}")
print(f"결과 : {result}")
print(f"메모리 : {memory}")
print(f"실행 시간 : {time}")
print(f"태그 : {tag}")
print(f"문제 링크 : https://www.acmicpc.net/problem/{problemID}")
