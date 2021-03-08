# Prefix Sum (누적 합)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

누적합은 단순히 이 알고리즘만 사용하는 문제보다 누적합과 다른 알고리즘을 섞어 쓰는 경우가 많습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7274)

|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/14929" target="_blank">귀찮아 (SIB)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/2167" target="_blank">2차원 배열의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/20438" target="_blank">출석체크</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/11660" target="_blank">구간 합 구하기 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/2015" target="_blank">수들의 합 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/10986" target="_blank">나머지 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/1749" target="_blank">점수따먹기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/20440" target="_blank">🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/20543" target="_blank">폭탄 던지는 태영이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 09 |                      | <a href="http://boj.kr/20116" target="_blank">상자의 균형</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 10 |                      | <a href="http://boj.kr/11659" target="_blank">구간 합 구하기 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 11 |                      | <a href="http://boj.kr/11441" target="_blank">합 구하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 12 |                      | <a href="http://boj.kr/17390" target="_blank">이건 꼭 풀어야 해!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 13 |                      | <a href="http://boj.kr/16139" target="_blank">인간-컴퓨터 상호작용</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 14 |                      | <a href="http://boj.kr/17123" target="_blank">배열 놀이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 15 |                      | <a href="http://boj.kr/16507" target="_blank">어두운 건 무서워</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 16 |                      | <a href="http://boj.kr/19951" target="_blank">태상이의 훈련소 생활</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 17 |                      | <a href="http://boj.kr/10427" target="_blank">빚</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 18 |                      | <a href="http://boj.kr/10713" target="_blank">기차 여행</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 19 |                      | <a href="http://boj.kr/20002" target="_blank">사과나무</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 20 |                      | <a href="http://boj.kr/20159" target="_blank">동작 그만. 밑장 빼기냐?</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |                      | <a href="http://boj.kr/18866" target="_blank">젊은 날의 생이여</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 22 |                      | <a href="http://boj.kr/5549" target="_blank">행성 탐사</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 23 |                      | <a href="http://boj.kr/2571" target="_blank">색종이 - 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |                      | <a href="http://boj.kr/3673" target="_blank">나눌 수 있는 부분 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 25 |                      | <a href="http://boj.kr/5875" target="_blank">오타</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 26 |                      | <a href="http://boj.kr/14476" target="_blank">최대공약수 하나 빼기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 27 |                      | <a href="http://boj.kr/19566" target="_blank">수열의 구간 평균</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/16971" target="_blank">배열 B의 값</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/2900" target="_blank">프로그램</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
