# Dynamic Programming 1 (동적계획법 1)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

다이나믹 프로그래밍 유형 쉬운 문제 위주로 뽑았습니다.

다이나믹 프로그래밍은 점화식을 세우면 절반 이상은 풀었다고 볼 수 있습니다.

점화식 세우는 건 금방 익히기 힘들어 코딩테스트에 나올만한 문제들,   
다이나믹 프로그래밍을 공부할만한 문제들을 최대한 뽑았습니다.

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7020)


|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/10870" target="_blank">피보나치 수 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> | <a href="./../solution/dynamic_programming_1/10870">바로가기</a> |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/2839" target="_blank">설탕 배달</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> | <a href="./../solution/dynamic_programming_1/2839">바로가기</a> |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/2748" target="_blank">피보나치 수 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> | <a href="./../solution/dynamic_programming_1/2748">바로가기</a> |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/1010" target="_blank">다리 놓기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/9655" target="_blank">돌 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/17626" target="_blank">Four Squares</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/1463" target="_blank">1로 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/9095" target="_blank">1, 2, 3 더하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/11726" target="_blank">2xn 타일링</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/2579" target="_blank">계단 오르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="http://boj.kr/11727" target="_blank">2xn 타일링 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="http://boj.kr/11053" target="_blank">가장 긴 증가하는 부분 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="http://boj.kr/1912" target="_blank">연속합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="http://boj.kr/9465" target="_blank">스티커</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="http://boj.kr/11055" target="_blank">가장 큰 증가 부분 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="http://boj.kr/1890" target="_blank">점프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="http://boj.kr/2407" target="_blank">조합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="http://boj.kr/15486" target="_blank">퇴사 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="http://boj.kr/1106" target="_blank">호텔</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="http://boj.kr/2156" target="_blank">포도주 시식</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="http://boj.kr/10844" target="_blank">쉬운 계단 수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="http://boj.kr/2293" target="_blank">동전 1</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="http://boj.kr/2294" target="_blank">동전</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="http://boj.kr/11660" target="_blank">구간 합 구하기 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 24 |                      | <a href="http://boj.kr/15489" target="_blank">파스칼 삼각형</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 25 |                      | <a href="http://boj.kr/14501" target="_blank">퇴사</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 26 |                      | <a href="http://boj.kr/2670" target="_blank">연속부분최대곱</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 27 |                      | <a href="http://boj.kr/13699" target="_blank">점화식</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/1003" target="_blank">피보나치 함수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/2193" target="_blank">이친수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/9461" target="_blank">파도반 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/1699" target="_blank">제곱수의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 32 |                      | <a href="http://boj.kr/15990" target="_blank">1, 2, 3 더하기 5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 33 |                      | <a href="http://boj.kr/10211" target="_blank">Maximum Subarray</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 34 |                      | <a href="http://boj.kr/17175" target="_blank">피보나치는 지겨웡~</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 35 |                      | <a href="http://boj.kr/15624" target="_blank">피보나치 수 7</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 36 |                      | <a href="http://boj.kr/17212" target="_blank">달나라 토끼를 위한 구매대금 지불 도우미</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 37 |                      | <a href="http://boj.kr/2876" target="_blank">그래픽스 퀴즈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 38 |                      | <a href="http://boj.kr/20152" target="_blank">Game Addiction</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 39 |                      | <a href="http://boj.kr/11722" target="_blank">가장 긴 감소하는 부분 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 40 |                      | <a href="http://boj.kr/1965" target="_blank">상자넣기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 41 |                      | <a href="http://boj.kr/11060" target="_blank">점프 점프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 42 |                      | <a href="http://boj.kr/15988" target="_blank">1, 2, 3 더하기 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 43 |                      | <a href="http://boj.kr/2491" target="_blank">수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 44 |                      | <a href="http://boj.kr/1660" target="_blank">캡틴 이다솜</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 45 |                      | <a href="http://boj.kr/14852" target="_blank">타일 채우기 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 46 |                      | <a href="http://boj.kr/14430" target="_blank">자원 캐기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 47 |                      | <a href="http://boj.kr/1633" target="_blank">최고의 팀 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 48 |                      | <a href="http://boj.kr/18353" target="_blank">병사 배치하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 49 |                      | <a href="http://boj.kr/17291" target="_blank">새끼치기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 50 |                      | <a href="http://boj.kr/4097" target="_blank">수익</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 51 |                      | <a href="http://boj.kr/20162" target="_blank">간식 파티</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 52 |                      | <a href="http://boj.kr/19622" target="_blank">회의실 배정 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 53 |                      | <a href="http://boj.kr/1149" target="_blank">RGB거리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 54 |                      | <a href="http://boj.kr/1932" target="_blank">정수 삼각형</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 55 |                      | <a href="http://boj.kr/11052" target="_blank">카드 구매하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 56 |                      | <a href="http://boj.kr/11057" target="_blank">오르막 수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 57 |                      | <a href="http://boj.kr/11051" target="_blank">이항 계수 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 58 |                      | <a href="http://boj.kr/11048" target="_blank">이동하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 59 |                      | <a href="http://boj.kr/1309" target="_blank">동물원</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 60 |                      | <a href="http://boj.kr/2565" target="_blank">전깃줄</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 61 |                      | <a href="http://boj.kr/2011" target="_blank">암호코드</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 62 |                      | <a href="http://boj.kr/10164" target="_blank">격자상의 경로</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 63 |                      | <a href="http://boj.kr/16194" target="_blank">카드 구매하기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 64 |                      | <a href="http://boj.kr/15989" target="_blank">1, 2, 3 더하기 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 65 |                      | <a href="http://boj.kr/12101" target="_blank">1, 2, 3 더하기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 66 |                      | <a href="http://boj.kr/15992" target="_blank">1, 2, 3 더하기 7</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 67 |                      | <a href="http://boj.kr/15991" target="_blank">1, 2, 3 더하기 6</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 68 |                      | <a href="http://boj.kr/16195" target="_blank">1, 2, 3 더하기 9</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 69 |                      | <a href="http://boj.kr/15993" target="_blank">1, 2, 3 더하기 8</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 70 |                      | <a href="http://boj.kr/1495" target="_blank">기타리스트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 71 |                      | <a href="http://boj.kr/2302" target="_blank">극장 좌석</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 72 |                      | <a href="http://boj.kr/11568" target="_blank">민균이의 계략</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 73 |                      | <a href="http://boj.kr/12026" target="_blank">BOJ 거리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 74 |                      | <a href="http://boj.kr/14722" target="_blank">우유 도시</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 75 |                      | <a href="http://boj.kr/13910" target="_blank">개업</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
