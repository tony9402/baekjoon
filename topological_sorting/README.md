# Topological Sorting (위상정렬)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

위상정렬 문제를 뽑아봤습니다.

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

계보 복원가 호석은 위상정렬로 말고 다른 풀이로도 풀이 가능합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7165)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14567" target="_blank">14567</a> | <a href="https://www.acmicpc.net/problem/14567" target="_blank">선수과목 (Prerequisite)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1005" target="_blank">1005</a> | <a href="https://www.acmicpc.net/problem/1005" target="_blank">ACM Craft</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2252" target="_blank">2252</a> | <a href="https://www.acmicpc.net/problem/2252" target="_blank">줄 세우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2623" target="_blank">2623</a> | <a href="https://www.acmicpc.net/problem/2623" target="_blank">음악프로그램</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1766" target="_blank">1766</a> | <a href="https://www.acmicpc.net/problem/1766" target="_blank">문제집</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 05 |                      | <a href="https://www.acmicpc.net/problem/2056" target="_blank">2056</a> | <a href="https://www.acmicpc.net/problem/2056" target="_blank">작업</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 06 |                      | <a href="https://www.acmicpc.net/problem/14676" target="_blank">14676</a> | <a href="https://www.acmicpc.net/problem/14676" target="_blank">영우는 사기꾼?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 07 |                      | <a href="https://www.acmicpc.net/problem/1516" target="_blank">1516</a> | <a href="https://www.acmicpc.net/problem/1516" target="_blank">게임 개발</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 08 |                      | <a href="https://www.acmicpc.net/problem/9470" target="_blank">9470</a> | <a href="https://www.acmicpc.net/problem/9470" target="_blank">Strahler 순서</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 09 |                      | <a href="https://www.acmicpc.net/problem/21276" target="_blank">21276</a> | <a href="https://www.acmicpc.net/problem/21276" target="_blank">계보 복원가 호석</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 10 |                      | <a href="https://www.acmicpc.net/problem/2637" target="_blank">2637</a> | <a href="https://www.acmicpc.net/problem/2637" target="_blank">장난감 조립</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 11 |                      | <a href="https://www.acmicpc.net/problem/20119" target="_blank">20119</a> | <a href="https://www.acmicpc.net/problem/20119" target="_blank">클레어와 물약</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
| 12 |                      | <a href="https://www.acmicpc.net/problem/3665" target="_blank">3665</a> | <a href="https://www.acmicpc.net/problem/3665" target="_blank">최종 순위</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
| 13 |                      | <a href="https://www.acmicpc.net/problem/1948" target="_blank">1948</a> | <a href="https://www.acmicpc.net/problem/1948" target="_blank">임계경로</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/> |                      |
