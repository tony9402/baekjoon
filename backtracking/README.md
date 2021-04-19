# Backtracking (백트래킹)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

백트래킹 문제를 뽑았습니다.

백트래킹의 기본 연습 문제인 N과 M 시리즈 모든 문제를 추천 문제로 뽑았습니다.

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7135)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  |  15649  | <a href="http://boj.kr/15649" target="_blank">N과 M (1)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 01 |  :heavy_check_mark:  |  15650  | <a href="http://boj.kr/15650" target="_blank">N과 M (2)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 02 |  :heavy_check_mark:  |  15651  | <a href="http://boj.kr/15651" target="_blank">N과 M (3)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 03 |  :heavy_check_mark:  |  15652  | <a href="http://boj.kr/15652" target="_blank">N과 M (4)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 04 |  :heavy_check_mark:  |  15654  | <a href="http://boj.kr/15654" target="_blank">N과 M (5)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 05 |  :heavy_check_mark:  |  15655  | <a href="http://boj.kr/15655" target="_blank">N과 M (6)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 06 |  :heavy_check_mark:  |  15656  | <a href="http://boj.kr/15656" target="_blank">N과 M (7)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 07 |  :heavy_check_mark:  |  15657  | <a href="http://boj.kr/15657" target="_blank">N과 M (8)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 08 |  :heavy_check_mark:  |  15663  | <a href="http://boj.kr/15663" target="_blank">N과 M (9)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 09 |  :heavy_check_mark:  |  15664  | <a href="http://boj.kr/15664" target="_blank">N과 M (10)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 10 |  :heavy_check_mark:  |  15665  | <a href="http://boj.kr/15665" target="_blank">N과 M (11)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 11 |  :heavy_check_mark:  |  15666  | <a href="http://boj.kr/15666" target="_blank">N과 M (12)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 12 |  :heavy_check_mark:  |  1182   | <a href="http://boj.kr/1182" target="_blank">부분수열의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 13 |  :heavy_check_mark:  |  10971  | <a href="http://boj.kr/10971" target="_blank">외판원 순회 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 14 |  :heavy_check_mark:  |  16987  | <a href="http://boj.kr/16987" target="_blank">계란으로 계란치기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 15 |  :heavy_check_mark:  |  14712  | <a href="http://boj.kr/14712" target="_blank">넴모넴모 (Easy)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> | <a href="./../solution/backtracking/14712">바로가기</a> |
| 16 |  :heavy_check_mark:  |  14888  | <a href="http://boj.kr/14888" target="_blank">연산자 끼워넣기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 17 |  :heavy_check_mark:  |  1174   | <a href="http://boj.kr/1174" target="_blank">줄어드는 숫자</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 18 |  :heavy_check_mark:  |  18430  | <a href="http://boj.kr/18430" target="_blank">무기 공학</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 19 |  :heavy_check_mark:  |  9663   | <a href="http://boj.kr/9663" target="_blank">N-Queen</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 20 |  :heavy_check_mark:  |  2580   | <a href="http://boj.kr/2580" target="_blank">스도쿠</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 21 |  :heavy_check_mark:  |  1062   | <a href="http://boj.kr/1062" target="_blank">가르침</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 22 |  :heavy_check_mark:  |  2661   | <a href="http://boj.kr/2661" target="_blank">좋은수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 23 |  :heavy_check_mark:  |  3980   | <a href="http://boj.kr/3980" target="_blank">선발 명단</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |  :heavy_check_mark:  |  6443   | <a href="http://boj.kr/6443" target="_blank">애너그램</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 25 |  :heavy_check_mark:  |  17136  | <a href="http://boj.kr/17136" target="_blank">색종이 붙이기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 26 |  :heavy_check_mark:  |  1799   | <a href="http://boj.kr/1799" target="_blank">비숍</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 27 |                      |  14889  | <a href="http://boj.kr/14889" target="_blank">스타트와 링크</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 28 |                      |  10974  | <a href="http://boj.kr/10974" target="_blank">모든 순열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 29 |                      |  15658  | <a href="http://boj.kr/15658" target="_blank">연산자 끼워넣기 (2)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 30 |                      |  16922  | <a href="http://boj.kr/16922" target="_blank">로마 숫자 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 31 |                      |  18429  | <a href="http://boj.kr/18429" target="_blank">근손실</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 32 |                      |  19949  | <a href="http://boj.kr/19949" target="_blank">영재의 시험</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 33 |                      |  1553   | <a href="http://boj.kr/1553" target="_blank">도미노 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 34 |                      |  20950  | <a href="http://boj.kr/20950" target="_blank">미술가 미미</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 35 |                      |  6603   | <a href="http://boj.kr/6603" target="_blank">로또</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 36 |                      |  10819  | <a href="http://boj.kr/10819" target="_blank">차이를 최대로</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 37 |                      |  2529   | <a href="http://boj.kr/2529" target="_blank">부등호</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 38 |                      |  19699  | <a href="http://boj.kr/19699" target="_blank">소-난다!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 39 |                      |  6987   | <a href="http://boj.kr/6987" target="_blank">월드컵</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 40 |                      |  16198  | <a href="http://boj.kr/16198" target="_blank">에너지 모으기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 41 |                      |  12101  | <a href="http://boj.kr/12101" target="_blank">1, 2, 3 더하기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 42 |                      |  10597  | <a href="http://boj.kr/10597" target="_blank">순열장난</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 43 |                      |  1189   | <a href="http://boj.kr/1189" target="_blank">컴백홈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 44 |                      |  19942  | <a href="http://boj.kr/19942" target="_blank">다이어트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 45 |                      |  18290  | <a href="http://boj.kr/18290" target="_blank">NM과 K (1)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 46 |                      |  1497   | <a href="http://boj.kr/1497" target="_blank">기타콘서트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 47 |                      |  15566  | <a href="http://boj.kr/15566" target="_blank">개구리 1</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 48 |                      |  1342   | <a href="http://boj.kr/1342" target="_blank">행운의 문자열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 49 |                      |  1759   | <a href="http://boj.kr/1759" target="_blank">암호 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 50 |                      |  1038   | <a href="http://boj.kr/1038" target="_blank">감소하는 수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 51 |                      |  2023   | <a href="http://boj.kr/2023" target="_blank">신기한 소수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 52 |                      |  1405   | <a href="http://boj.kr/1405" target="_blank">미친 로봇</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 53 |                      |  7490   | <a href="http://boj.kr/7490" target="_blank">0 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 54 |                      |  13908  | <a href="http://boj.kr/13908" target="_blank">비밀번호</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 55 |                      |  7682   | <a href="http://boj.kr/7682" target="_blank">틱택토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 56 |                      |  20208  | <a href="http://boj.kr/20208" target="_blank">진우의 민트초코우유</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 57 |                      |  1469   | <a href="http://boj.kr/1469" target="_blank">숌 사이 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 58 |                      |  10421  | <a href="http://boj.kr/10421" target="_blank">수식 완성하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 59 |                      |  15684  | <a href="http://boj.kr/15684" target="_blank">사다리 조작</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 60 |                      |  1987   | <a href="http://boj.kr/1987" target="_blank">알파벳</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 61 |                      |  2239   | <a href="http://boj.kr/2239" target="_blank">스도쿠</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 62 |                      |  16938  | <a href="http://boj.kr/16938" target="_blank">캠프 준비</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 63 |                      |  2922   | <a href="http://boj.kr/2922" target="_blank">즐거운 단어</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 64 |                      |  15918  | <a href="http://boj.kr/15918" target="_blank">랭퍼든 수열쟁이야!!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 65 |                      |  1941   | <a href="http://boj.kr/1941" target="_blank">소문난 칠공주</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 66 |                      |  1248   | <a href="http://boj.kr/1248" target="_blank">맞춰봐</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 67 |                      |  9944   | <a href="http://boj.kr/9944" target="_blank">NxM 보드 완주하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 68 |                      |  2026   | <a href="http://boj.kr/2026" target="_blank">소풍</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 69 |                      |  15659  | <a href="http://boj.kr/15659" target="_blank">연산자 끼워넣기 (3)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 70 |                      |  12908  | <a href="http://boj.kr/12908" target="_blank">텔레포트 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 71 |                      |  16571  | <a href="http://boj.kr/16571" target="_blank">알파 틱택토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 72 |                      |  3165   | <a href="http://boj.kr/3165" target="_blank">5</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 73 |                      |  1729   | <a href="http://boj.kr/1729" target="_blank">이차원 배열의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
