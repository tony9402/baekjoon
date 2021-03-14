# Two Pointers (투 포인터)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

최근 많이 나오는 유형이니 꼭 풀어보시길 바랍니다.

특히, 투 포인터는 부분합과 많이 연관되어 나오는 만큼, 투 포인터 문제는 아니지만 부분합을 연습할 수 있는 문제를 첫 문제로 넣어놨습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6782)

|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/11728" target="_blank">배열 합치기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/11659" target="_blank">구간 합 구하기 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/20922" target="_blank">겹치는 건 싫어</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/2470" target="_blank">두 용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/15961" target="_blank">회전 초밥</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/1806" target="_blank">부분합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/20366" target="_blank">같이 눈사람 만들래?</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/3151" target="_blank">합이 0</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/20442" target="_blank">ㅋㅋ루ㅋㅋ</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 10 |                      | <a href="http://boj.kr/2018" target="_blank">수들의 합 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 11 |                      | <a href="http://boj.kr/1940" target="_blank">주몽</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 12 |                      | <a href="http://boj.kr/3273" target="_blank">두 수의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 13 |                      | <a href="http://boj.kr/10025" target="_blank">게으른 백곰</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 14 |                      | <a href="http://boj.kr/6159" target="_blank">코스튬 파티</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 15 |                      | <a href="http://boj.kr/2003" target="_blank">수들의 합 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 16 |                      | <a href="http://boj.kr/2559" target="_blank">수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 17 |                      | <a href="http://boj.kr/15565" target="_blank">귀여운 라이언</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 18 |                      | <a href="http://boj.kr/2531" target="_blank">회전 초밥</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 19 |                      | <a href="http://boj.kr/2118" target="_blank">두 개의 탑</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 20 |                      | <a href="http://boj.kr/2467" target="_blank">용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |                      | <a href="http://boj.kr/2230" target="_blank">수 고르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 22 |                      | <a href="http://boj.kr/14921" target="_blank">용액 합성하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 23 |                      | <a href="http://boj.kr/9024" target="_blank">두 수의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 24 |                      | <a href="http://boj.kr/2473" target="_blank">세 용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 25 |                      | <a href="http://boj.kr/1484" target="_blank">다이어트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 26 |                      | <a href="http://boj.kr/13422" target="_blank">도둑</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 27 |                      | <a href="http://boj.kr/1644" target="_blank">소수의 연속합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/15831" target="_blank">준표의 조약돌</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/6137" target="_blank">문자열 생성</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/20181" target="_blank">꿈틀꿈틀 호석 애벌레 - 효율성</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/16472" target="_blank">고냥이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
