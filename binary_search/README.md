# Binary Search (이분탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7277)
|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/1789" target="_blank">수들의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/2417" target="_blank">정수 제곱근</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/10815" target="_blank">숫자 카드</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/2805" target="_blank">나무 자르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/1654" target="_blank">랜선 자르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/2512" target="_blank">예산</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/19637" target="_blank">IF문 좀 대신 써줘</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/11663" target="_blank">선분 위의 점</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/2110" target="_blank">공유기 설치</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/3079" target="_blank">입국심사</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="http://boj.kr/2470" target="_blank">두 용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="http://boj.kr/1477" target="_blank">휴게소 세우기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="http://boj.kr/20444" target="_blank">색종이와 가위</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="http://boj.kr/1939" target="_blank">중량제한</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="http://boj.kr/2473" target="_blank">세 용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="http://boj.kr/13397" target="_blank">구간 나누기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="http://boj.kr/2412" target="_blank">암벽 등반</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="http://boj.kr/1300" target="_blank">K번째 수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="http://boj.kr/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 19 |                      | <a href="http://boj.kr/17266" target="_blank">어두운 굴다리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 20 |                      | <a href="http://boj.kr/1920" target="_blank">수 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 21 |                      | <a href="http://boj.kr/10816" target="_blank">숫자 카드 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 22 |                      | <a href="http://boj.kr/2428" target="_blank">표절</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 23 |                      | <a href="http://boj.kr/20551" target="_blank">Sort 마스터 배지훈의 후계자</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 24 |                      | <a href="http://boj.kr/1072" target="_blank">게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 25 |                      | <a href="http://boj.kr/2776" target="_blank">암기왕</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 26 |                      | <a href="http://boj.kr/6236" target="_blank">용돈 관리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 27 |                      | <a href="http://boj.kr/7795" target="_blank">먹을 것인가 먹힐 것인가</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/2792" target="_blank">보석 상자</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/16401" target="_blank">과자 나눠주기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/13702" target="_blank">이상한 술집</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/11561" target="_blank">징검다리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 32 |                      | <a href="http://boj.kr/14627" target="_blank">파닭파닭</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 33 |                      | <a href="http://boj.kr/1166" target="_blank">선물</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 34 |                      | <a href="http://boj.kr/17451" target="_blank">평행 우주</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 35 |                      | <a href="http://boj.kr/17393" target="_blank">다이나믹 롤러</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 36 |                      | <a href="http://boj.kr/17124" target="_blank">두 개의 배열</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 37 |                      | <a href="http://boj.kr/15810" target="_blank">풍선 공장</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 38 |                      | <a href="http://boj.kr/17503" target="_blank">맥주 축제</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 39 |                      | <a href="http://boj.kr/18113" target="_blank">그르다 김가놈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 40 |                      | <a href="http://boj.kr/2121" target="_blank">넷이 놀기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 41 |                      | <a href="http://boj.kr/2343" target="_blank">기타 레슨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 42 |                      | <a href="http://boj.kr/2022" target="_blank">사다리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 43 |                      | <a href="http://boj.kr/16564" target="_blank">히오스 프로게이머</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 44 |                      | <a href="http://boj.kr/11687" target="_blank">팩토리얼 0의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 45 |                      | <a href="http://boj.kr/18114" target="_blank">블랙 프라이데이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 46 |                      | <a href="http://boj.kr/14575" target="_blank">뒤풀이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 47 |                      | <a href="http://boj.kr/17179" target="_blank">케이크 자르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 48 |                      | <a href="http://boj.kr/16960" target="_blank">스위치와 램프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 49 |                      | <a href="http://boj.kr/20495" target="_blank">수열과 헌팅</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 50 |                      | <a href="http://boj.kr/3020" target="_blank">개똥벌레</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 51 |                      | <a href="http://boj.kr/2467" target="_blank">용액</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 52 |                      | <a href="http://boj.kr/2866" target="_blank">문자열 잘라내기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 53 |                      | <a href="http://boj.kr/9024" target="_blank">두 수의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 54 |                      | <a href="http://boj.kr/8983" target="_blank">사냥꾼</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 55 |                      | <a href="http://boj.kr/9007" target="_blank">카누 선수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 56 |                      | <a href="http://boj.kr/17951" target="_blank">흩날리는 시험지 속에서 내 평점이 느껴진거야</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 57 |                      | <a href="http://boj.kr/12757" target="_blank">전설의 JBNU</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 58 |                      | <a href="http://boj.kr/2143" target="_blank">두 배열의 합</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 59 |                      | <a href="http://boj.kr/16434" target="_blank">드래곤 앤 던전</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 60 |                      | <a href="http://boj.kr/15823" target="_blank">카드 팩 구매하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 61 |                      | <a href="http://boj.kr/2613" target="_blank">숫자구슬</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 62 |                      | <a href="http://boj.kr/1561" target="_blank">놀이 공원</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 63 |                      | <a href="http://boj.kr/15732" target="_blank">도토리 숨기기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 64 |                      | <a href="http://boj.kr/6209" target="_blank">제자리 멀리뛰기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
