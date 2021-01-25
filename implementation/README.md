# Implementation (구현)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

시뮬레이션 관련 문제는 시뮬레이션에 있습니다.

(매우 [단순한 구현](https://www.acmicpc.net/problem/1000)는 추가하지 않았습니다.)

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6783)

|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/1212" target="_blank">8진수 2진수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/2.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/2753" target="_blank">윤년</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/2.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/20053" target="_blank">최소, 최대 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/3.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/5597" target="_blank">과제 안 내신 분..?</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/20546" target="_blank">🐜 기적의 매매법 🐜</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/1783" target="_blank">병든 나이트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/1913" target="_blank">달팽이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/14467" target="_blank">소가 길을 건너간 이유 1</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/12933" target="_blank">오리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/2578" target="_blank">빙고</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="http://boj.kr/4396" target="_blank">지뢰 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="http://boj.kr/1244" target="_blank">스위치 켜고 끄기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="http://boj.kr/10994" target="_blank">별 찍기 - 19</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="http://boj.kr/20291" target="_blank">파일 정리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="http://boj.kr/20436" target="_blank">ZOAC 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="http://boj.kr/16926" target="_blank">배열 돌리기 1</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="http://boj.kr/17413" target="_blank">단어 뒤집기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="http://boj.kr/2615" target="_blank">오목</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="http://boj.kr/17276" target="_blank">배열 돌리기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="http://boj.kr/15787" target="_blank">기차가 어둠을 헤치고 은하수를</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="http://boj.kr/20164" target="_blank">홀수 홀릭 호석</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="http://boj.kr/20207" target="_blank">달력</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="http://boj.kr/14719" target="_blank">빗물</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="http://boj.kr/16719" target="_blank">ZOAC</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 24 |                      | <a href="http://boj.kr/1316" target="_blank">그룹 단어 체커</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 25 |                      | <a href="http://boj.kr/18311" target="_blank">왕복</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 26 |                      | <a href="http://boj.kr/5766" target="_blank">할아버지는 유명해!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 27 |                      | <a href="http://boj.kr/2729" target="_blank">이진수 덧셈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/16935" target="_blank">배열 돌리기 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/17128" target="_blank">소가 정보섬에 올라온 이유</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/1283" target="_blank">단축키 지정</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/10703" target="_blank">유성</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 32 |                      | <a href="http://boj.kr/16927" target="_blank">배열 돌리기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 33 |                      | <a href="http://boj.kr/9934" target="_blank">완전 이진 트리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 34 |                      | <a href="http://boj.kr/2469" target="_blank">사다리 타기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 35 |                      | <a href="http://boj.kr/2877" target="_blank">4와 7</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 36 |                      | <a href="http://boj.kr/20327" target="_blank">배열 돌리기 6</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 37 |                      | <a href="http://boj.kr/15886" target="_blank">내 선물을 받아줘 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 38 |                      | <a href="http://boj.kr/17406" target="_blank">배열 돌리기 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 39 |                      | <a href="http://boj.kr/1022" target="_blank">소용돌이 예쁘게 출력하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 40 |                      | <a href="http://boj.kr/9081" target="_blank">단어 맞추기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 41 |                      | <a href="http://boj.kr/17470" target="_blank">배열 돌리기 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 42 |                      | <a href="http://boj.kr/15806" target="_blank">영우의 기숙사 청소</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
