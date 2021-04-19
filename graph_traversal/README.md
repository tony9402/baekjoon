# Graph Traversal (그래프 탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

BFS, DFS 유형을 다양하게 골랐습니다. 

문제를 보고 어떤 알고리즘을 써야할지 잘 판단하셔야 합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6853)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  |  2606   | <a href="http://boj.kr/2606" target="_blank">바이러스</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 01 |  :heavy_check_mark:  |  1260   | <a href="http://boj.kr/1260" target="_blank">DFS와 BFS</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 02 |  :heavy_check_mark:  |  11725  | <a href="http://boj.kr/11725" target="_blank">트리의 부모 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 03 |  :heavy_check_mark:  |  1325   | <a href="http://boj.kr/1325" target="_blank">효율적인 해킹</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 04 |  :heavy_check_mark:  |  2178   | <a href="http://boj.kr/2178" target="_blank">미로 탐색</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 05 |  :heavy_check_mark:  |  2667   | <a href="http://boj.kr/2667" target="_blank">단지번호붙이기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 06 |  :heavy_check_mark:  |  7576   | <a href="http://boj.kr/7576" target="_blank">토마토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 07 |  :heavy_check_mark:  |  7569   | <a href="http://boj.kr/7569" target="_blank">토마토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 08 |  :heavy_check_mark:  |  16918  | <a href="http://boj.kr/16918" target="_blank">봄버맨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 09 |  :heavy_check_mark:  |  5547   | <a href="http://boj.kr/5547" target="_blank">일루미네이션</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 10 |  :heavy_check_mark:  |  14502  | <a href="http://boj.kr/14502" target="_blank">연구소</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 11 |  :heavy_check_mark:  |  16234  | <a href="http://boj.kr/16234" target="_blank">인구 이동</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 12 |  :heavy_check_mark:  |  2636   | <a href="http://boj.kr/2636" target="_blank">치즈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 13 |  :heavy_check_mark:  |  13549  | <a href="http://boj.kr/13549" target="_blank">숨바꼭질 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 14 |  :heavy_check_mark:  |  1600   | <a href="http://boj.kr/1600" target="_blank">말이 되고픈 원숭이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 15 |  :heavy_check_mark:  |  17836  | <a href="http://boj.kr/17836" target="_blank">공주님을 구해라!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 16 |  :heavy_check_mark:  |  16973  | <a href="http://boj.kr/16973" target="_blank">직사각형 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 17 |  :heavy_check_mark:  |  14940  | <a href="http://boj.kr/14940" target="_blank">쉬운 최단거리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 18 |  :heavy_check_mark:  |  18513  | <a href="http://boj.kr/18513" target="_blank">샘터</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/graph_traversal/18513">바로가기</a> |
| 19 |  :heavy_check_mark:  |  2668   | <a href="http://boj.kr/2668" target="_blank">숫자고르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 20 |  :heavy_check_mark:  |  13023  | <a href="http://boj.kr/13023" target="_blank">ABCDE</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |  :heavy_check_mark:  |  16954  | <a href="http://boj.kr/16954" target="_blank">움직이는 미로 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 22 |  :heavy_check_mark:  |  2206   | <a href="http://boj.kr/2206" target="_blank">벽 부수고 이동하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 23 |  :heavy_check_mark:  |  2573   | <a href="http://boj.kr/2573" target="_blank">빙산</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |  :heavy_check_mark:  |  4179   | <a href="http://boj.kr/4179" target="_blank">불!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 25 |  :heavy_check_mark:  |  16932  | <a href="http://boj.kr/16932" target="_blank">모양 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 26 |  :heavy_check_mark:  |  9466   | <a href="http://boj.kr/9466" target="_blank">텀 프로젝트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 27 |  :heavy_check_mark:  |  1967   | <a href="http://boj.kr/1967" target="_blank">트리의 지름</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 28 |                      |  16956  | <a href="http://boj.kr/16956" target="_blank">늑대와 양</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 29 |                      |  1012   | <a href="http://boj.kr/1012" target="_blank">유기농 배추</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 30 |                      |  11724  | <a href="http://boj.kr/11724" target="_blank">연결 요소의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 31 |                      |  4963   | <a href="http://boj.kr/4963" target="_blank">섬의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 32 |                      |  7562   | <a href="http://boj.kr/7562" target="_blank">나이트의 이동</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 33 |                      |  2644   | <a href="http://boj.kr/2644" target="_blank">촌수계산</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 34 |                      |  3184   | <a href="http://boj.kr/3184" target="_blank">양</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 35 |                      |  18352  | <a href="http://boj.kr/18352" target="_blank">특정 거리의 도시 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 36 |                      |  13565  | <a href="http://boj.kr/13565" target="_blank">침투</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 37 |                      |  12761  | <a href="http://boj.kr/12761" target="_blank">돌다리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 38 |                      |  3187   | <a href="http://boj.kr/3187" target="_blank">양치기 꿍</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 39 |                      |  18232  | <a href="http://boj.kr/18232" target="_blank">텔레포트 정거장</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 40 |                      |  14248  | <a href="http://boj.kr/14248" target="_blank">점프 점프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 41 |                      |  17086  | <a href="http://boj.kr/17086" target="_blank">아기 상어 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 42 |                      |  16928  | <a href="http://boj.kr/16928" target="_blank">뱀과 사다리 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 43 |                      |  1697   | <a href="http://boj.kr/1697" target="_blank">숨바꼭질</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 44 |                      |  2583   | <a href="http://boj.kr/2583" target="_blank">영역 구하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 45 |                      |  5567   | <a href="http://boj.kr/5567" target="_blank">결혼식</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 46 |                      |  1926   | <a href="http://boj.kr/1926" target="_blank">그림</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 47 |                      |  1743   | <a href="http://boj.kr/1743" target="_blank">음식물 피하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 48 |                      |  6118   | <a href="http://boj.kr/6118" target="_blank">숨바꼭질</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 49 |                      |  16953  | <a href="http://boj.kr/16953" target="_blank">A → B</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 50 |                      |  16948  | <a href="http://boj.kr/16948" target="_blank">데스 나이트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 51 |                      |  18405  | <a href="http://boj.kr/18405" target="_blank">경쟁적 전염</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 52 |                      |  15558  | <a href="http://boj.kr/15558" target="_blank">점프 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 53 |                      |  1303   | <a href="http://boj.kr/1303" target="_blank">전쟁 - 전투</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 54 |                      |  14496  | <a href="http://boj.kr/14496" target="_blank">그대, 그머가 되어</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 55 |                      |  11123  | <a href="http://boj.kr/11123" target="_blank">양 한마리... 양 두마리...</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 56 |                      |  18404  | <a href="http://boj.kr/18404" target="_blank">현명한 나이트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 57 |                      |  14716  | <a href="http://boj.kr/14716" target="_blank">현수막</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 58 |                      |  1068   | <a href="http://boj.kr/1068" target="_blank">트리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 59 |                      |  1058   | <a href="http://boj.kr/1058" target="_blank">친구</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 60 |                      |  10026  | <a href="http://boj.kr/10026" target="_blank">적록색약</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 61 |                      |  3055   | <a href="http://boj.kr/3055" target="_blank">탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 62 |                      |  5014   | <a href="http://boj.kr/5014" target="_blank">스타트링크</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 63 |                      |  2589   | <a href="http://boj.kr/2589" target="_blank">보물섬</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 64 |                      |  9019   | <a href="http://boj.kr/9019" target="_blank">DSLR</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 65 |                      |  11559  | <a href="http://boj.kr/11559" target="_blank">Puyo Puyo</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 66 |                      |  12851  | <a href="http://boj.kr/12851" target="_blank">숨바꼭질 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 67 |                      |  17141  | <a href="http://boj.kr/17141" target="_blank">연구소 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 68 |                      |  17129  | <a href="http://boj.kr/17129" target="_blank">윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 69 |                      |  16174  | <a href="http://boj.kr/16174" target="_blank">점프왕 쩰리 (Large)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 70 |                      |  2194   | <a href="http://boj.kr/2194" target="_blank">유닛 이동시키기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 71 |                      |  16432  | <a href="http://boj.kr/16432" target="_blank">떡장수와 호랑이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 72 |                      |  1707   | <a href="http://boj.kr/1707" target="_blank">이분 그래프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 73 |                      |  17142  | <a href="http://boj.kr/17142" target="_blank">연구소 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 74 |                      |  5427   | <a href="http://boj.kr/5427" target="_blank">불</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 75 |                      |  13913  | <a href="http://boj.kr/13913" target="_blank">숨바꼭질 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 76 |                      |  2638   | <a href="http://boj.kr/2638" target="_blank">치즈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 77 |                      |  2665   | <a href="http://boj.kr/2665" target="_blank">미로만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 78 |                      |  1726   | <a href="http://boj.kr/1726" target="_blank">로봇</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 79 |                      |  2234   | <a href="http://boj.kr/2234" target="_blank">성곽</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 80 |                      |  6087   | <a href="http://boj.kr/6087" target="_blank">레이저 통신</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 81 |                      |  2151   | <a href="http://boj.kr/2151" target="_blank">거울 설치</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 82 |                      |  14923  | <a href="http://boj.kr/14923" target="_blank">미로 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 83 |                      |  2146   | <a href="http://boj.kr/2146" target="_blank">다리 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 84 |                      |  14442  | <a href="http://boj.kr/14442" target="_blank">벽 부수고 이동하기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 85 |                      |  10711  | <a href="http://boj.kr/10711" target="_blank">모래성</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 86 |                      |  16947  | <a href="http://boj.kr/16947" target="_blank">서울 지하철 2호선</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 87 |                      |  16988  | <a href="http://boj.kr/16988" target="_blank">Baaaaaaaaaduk2 (Easy)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 88 |                      |  16985  | <a href="http://boj.kr/16985" target="_blank">Maaaaaaaaaze</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 89 |                      |  17616  | <a href="http://boj.kr/17616" target="_blank">등수 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
