# Brute Force (완전탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

완전탐색 중 백트래킹 있었던 문제와 최대한 겹치지 않도록 했습니다.

다른 알고리즘 풀었어도 완전탐색으로 풀어보시면 좋습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7271)
|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/2798" target="_blank">블랙잭</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/2231" target="_blank">분해합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/19532" target="_blank">수학은 비대면강의입니다</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/18312" target="_blank">시각</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/15721" target="_blank">번데기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/1969" target="_blank">DNA</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/2503" target="_blank">숫자 야구</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/2422" target="_blank">한윤정이 이탈리아에 가서 아이스크림을 사먹는데</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/17626" target="_blank">Four Squares</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/5568" target="_blank">카드 놓기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="http://boj.kr/18511" target="_blank">큰 수 구성하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="http://boj.kr/9079" target="_blank">동전 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="http://boj.kr/14501" target="_blank">퇴사</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="http://boj.kr/16937" target="_blank">두 스티커</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="http://boj.kr/2615" target="_blank">오목</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="http://boj.kr/16439" target="_blank">치킨치킨치킨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="http://boj.kr/16508" target="_blank">전공책</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="http://boj.kr/14620" target="_blank">꽃길</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="http://boj.kr/12919" target="_blank">A와 B 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="http://boj.kr/1548" target="_blank">부분 삼각 수열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="http://boj.kr/2961" target="_blank">도영이가 만든 맛있는 음식</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="http://boj.kr/15661" target="_blank">링크와 스타트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="http://boj.kr/1025" target="_blank">제곱수 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="http://boj.kr/14500" target="_blank">테트로미노</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 24 |  :heavy_check_mark:  | <a href="http://boj.kr/15686" target="_blank">치킨 배달</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 25 |  :heavy_check_mark:  | <a href="http://boj.kr/21278" target="_blank">호석이 두 마리 치킨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 26 |  :heavy_check_mark:  | <a href="http://boj.kr/21315" target="_blank">카드 섞기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 27 |  :heavy_check_mark:  | <a href="http://boj.kr/16637" target="_blank">괄호 추가하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 28 |  :heavy_check_mark:  | <a href="http://boj.kr/14391" target="_blank">종이 조각</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 29 |  :heavy_check_mark:  | <a href="http://boj.kr/18808" target="_blank">스티커 붙이기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/9094" target="_blank">수학적 호기심</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/3.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/4690" target="_blank">완전 세제곱</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/3.svg"/> |                      |
| 32 |                      | <a href="http://boj.kr/3040" target="_blank">백설 공주와 일곱 난쟁이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 33 |                      | <a href="http://boj.kr/10448" target="_blank">유레카 이론</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 34 |                      | <a href="http://boj.kr/2309" target="_blank">일곱 난쟁이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 35 |                      | <a href="http://boj.kr/14697" target="_blank">방 배정하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 36 |                      | <a href="http://boj.kr/1668" target="_blank">트로피 진열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 37 |                      | <a href="http://boj.kr/13410" target="_blank">거꾸로 구구단</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/4.svg"/> |                      |
| 38 |                      | <a href="http://boj.kr/1145" target="_blank">적어도 대부분의 배수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 39 |                      | <a href="http://boj.kr/2160" target="_blank">그림 비교</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 40 |                      | <a href="http://boj.kr/18512" target="_blank">점프 점프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 41 |                      | <a href="http://boj.kr/18868" target="_blank">멀티버스 Ⅰ</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/5.svg"/> |                      |
| 42 |                      | <a href="http://boj.kr/1436" target="_blank">영화감독 숌</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 43 |                      | <a href="http://boj.kr/1018" target="_blank">체스판 다시 칠하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 44 |                      | <a href="http://boj.kr/7568" target="_blank">덩치</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 45 |                      | <a href="http://boj.kr/2435" target="_blank">기상청 인턴 신현수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 46 |                      | <a href="http://boj.kr/2635" target="_blank">수 이어가기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 47 |                      | <a href="http://boj.kr/1059" target="_blank">좋은 구간</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 48 |                      | <a href="http://boj.kr/11170" target="_blank">0의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 49 |                      | <a href="http://boj.kr/1251" target="_blank">단어 나누기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 50 |                      | <a href="http://boj.kr/14912" target="_blank">숫자 빈도수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 51 |                      | <a href="http://boj.kr/17521" target="_blank">Byte Coin</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 52 |                      | <a href="http://boj.kr/19947" target="_blank">투자의 귀재 배주형</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 53 |                      | <a href="http://boj.kr/1359" target="_blank">복권</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 54 |                      | <a href="http://boj.kr/15779" target="_blank">Zigzag</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 55 |                      | <a href="http://boj.kr/17484" target="_blank">진우의 달 여행 (Small)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 56 |                      | <a href="http://boj.kr/4096" target="_blank">팰린드로미터</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 57 |                      | <a href="http://boj.kr/1065" target="_blank">한수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 58 |                      | <a href="http://boj.kr/1120" target="_blank">문자열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 59 |                      | <a href="http://boj.kr/3085" target="_blank">사탕 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 60 |                      | <a href="http://boj.kr/1543" target="_blank">문서 검색</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 61 |                      | <a href="http://boj.kr/15970" target="_blank">화살표 그리기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 62 |                      | <a href="http://boj.kr/5671" target="_blank">호텔 방 번호</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 63 |                      | <a href="http://boj.kr/5883" target="_blank">아이폰 9S</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 64 |                      | <a href="http://boj.kr/16951" target="_blank">블록 놀이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 65 |                      | <a href="http://boj.kr/15270" target="_blank">친구 팰린드롬</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 66 |                      | <a href="http://boj.kr/1487" target="_blank">물건 팔기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 67 |                      | <a href="http://boj.kr/11502" target="_blank">세 개의 소수 문제</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 68 |                      | <a href="http://boj.kr/9996" target="_blank">한국이 그리울 땐 서버에 접속하지</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 69 |                      | <a href="http://boj.kr/10472" target="_blank">십자뒤집기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 70 |                      | <a href="http://boj.kr/1895" target="_blank">필터</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 71 |                      | <a href="http://boj.kr/19949" target="_blank">영재의 시험</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 72 |                      | <a href="http://boj.kr/15728" target="_blank">에리 - 카드</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 73 |                      | <a href="http://boj.kr/1503" target="_blank">세 수 고르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 74 |                      | <a href="http://boj.kr/1421" target="_blank">나무꾼 이다솜</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 75 |                      | <a href="http://boj.kr/1411" target="_blank">비슷한 단어</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 76 |                      | <a href="http://boj.kr/1254" target="_blank">팰린드롬 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 77 |                      | <a href="http://boj.kr/1527" target="_blank">금민수의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 78 |                      | <a href="http://boj.kr/17610" target="_blank">양팔저울</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 79 |                      | <a href="http://boj.kr/16943" target="_blank">숫자 재배치</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 80 |                      | <a href="http://boj.kr/17085" target="_blank">십자가 2개 놓기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 81 |                      | <a href="http://boj.kr/1107" target="_blank">리모컨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 82 |                      | <a href="http://boj.kr/17471" target="_blank">게리맨더링</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 83 |                      | <a href="http://boj.kr/1747" target="_blank">소수&팰린드롬</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 84 |                      | <a href="http://boj.kr/14225" target="_blank">부분수열의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 85 |                      | <a href="http://boj.kr/1034" target="_blank">램프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 86 |                      | <a href="http://boj.kr/1711" target="_blank">직각삼각형</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 87 |                      | <a href="http://boj.kr/16986" target="_blank">인싸들의 가위바위보</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 88 |                      | <a href="http://boj.kr/1581" target="_blank">락스타 락동호</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
