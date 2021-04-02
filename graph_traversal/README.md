# Graph Traversal (그래프 탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

BFS, DFS 유형을 다양하게 골랐습니다. 

문제를 보고 어떤 알고리즘을 써야할지 잘 판단하셔야 합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6853)
|          순번          |        추천 문제         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="http://boj.kr/2606" target="_blank">바이러스</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="http://boj.kr/1260" target="_blank">DFS와 BFS</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="http://boj.kr/11725" target="_blank">트리의 부모 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 03 |  :heavy_check_mark:  | <a href="http://boj.kr/1325" target="_blank">효율적인 해킹</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="http://boj.kr/2178" target="_blank">미로 탐색</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="http://boj.kr/2667" target="_blank">단지번호붙이기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 06 |  :heavy_check_mark:  | <a href="http://boj.kr/7576" target="_blank">토마토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="http://boj.kr/7569" target="_blank">토마토</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="http://boj.kr/16918" target="_blank">봄버맨</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="http://boj.kr/5547" target="_blank">일루미네이션</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="http://boj.kr/14502" target="_blank">연구소</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="http://boj.kr/16234" target="_blank">인구 이동</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="http://boj.kr/2636" target="_blank">치즈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="http://boj.kr/13549" target="_blank">숨바꼭질 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="http://boj.kr/1600" target="_blank">말이 되고픈 원숭이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="http://boj.kr/17836" target="_blank">공주님을 구해라!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="http://boj.kr/16973" target="_blank">직사각형 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="http://boj.kr/14940" target="_blank">쉬운 최단거리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="http://boj.kr/18513" target="_blank">샘터</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="http://boj.kr/2668" target="_blank">숫자고르기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="http://boj.kr/13023" target="_blank">ABCDE</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="http://boj.kr/16954" target="_blank">움직이는 미로 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="http://boj.kr/2206" target="_blank">벽 부수고 이동하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="http://boj.kr/2573" target="_blank">빙산</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |  :heavy_check_mark:  | <a href="http://boj.kr/4179" target="_blank">불!</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 25 |  :heavy_check_mark:  | <a href="http://boj.kr/16932" target="_blank">모양 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 26 |  :heavy_check_mark:  | <a href="http://boj.kr/9466" target="_blank">텀 프로젝트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 27 |  :heavy_check_mark:  | <a href="http://boj.kr/1967" target="_blank">트리의 지름</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 28 |                      | <a href="http://boj.kr/16956" target="_blank">늑대와 양</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 29 |                      | <a href="http://boj.kr/1012" target="_blank">유기농 배추</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 30 |                      | <a href="http://boj.kr/11724" target="_blank">연결 요소의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 31 |                      | <a href="http://boj.kr/4963" target="_blank">섬의 개수</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 32 |                      | <a href="http://boj.kr/7562" target="_blank">나이트의 이동</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 33 |                      | <a href="http://boj.kr/2644" target="_blank">촌수계산</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 34 |                      | <a href="http://boj.kr/3184" target="_blank">양</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 35 |                      | <a href="http://boj.kr/18352" target="_blank">특정 거리의 도시 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 36 |                      | <a href="http://boj.kr/13565" target="_blank">침투</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 37 |                      | <a href="http://boj.kr/12761" target="_blank">돌다리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 38 |                      | <a href="http://boj.kr/3187" target="_blank">양치기 꿍</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 39 |                      | <a href="http://boj.kr/18232" target="_blank">텔레포트 정거장</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 40 |                      | <a href="http://boj.kr/14248" target="_blank">점프 점프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 41 |                      | <a href="http://boj.kr/17086" target="_blank">아기 상어 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 42 |                      | <a href="http://boj.kr/16928" target="_blank">뱀과 사다리 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 43 |                      | <a href="http://boj.kr/1697" target="_blank">숨바꼭질</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 44 |                      | <a href="http://boj.kr/2583" target="_blank">영역 구하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 45 |                      | <a href="http://boj.kr/5567" target="_blank">결혼식</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 46 |                      | <a href="http://boj.kr/1926" target="_blank">그림</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 47 |                      | <a href="http://boj.kr/1743" target="_blank">음식물 피하기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 48 |                      | <a href="http://boj.kr/6118" target="_blank">숨바꼭질</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 49 |                      | <a href="http://boj.kr/16953" target="_blank">A → B</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 50 |                      | <a href="http://boj.kr/16948" target="_blank">데스 나이트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 51 |                      | <a href="http://boj.kr/18405" target="_blank">경쟁적 전염</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 52 |                      | <a href="http://boj.kr/15558" target="_blank">점프 게임</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 53 |                      | <a href="http://boj.kr/1303" target="_blank">전쟁 - 전투</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 54 |                      | <a href="http://boj.kr/14496" target="_blank">그대, 그머가 되어</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 55 |                      | <a href="http://boj.kr/11123" target="_blank">양 한마리... 양 두마리...</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 56 |                      | <a href="http://boj.kr/18404" target="_blank">현명한 나이트</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 57 |                      | <a href="http://boj.kr/14716" target="_blank">현수막</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 58 |                      | <a href="http://boj.kr/1068" target="_blank">트리</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 59 |                      | <a href="http://boj.kr/1058" target="_blank">친구</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 60 |                      | <a href="http://boj.kr/10026" target="_blank">적록색약</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 61 |                      | <a href="http://boj.kr/3055" target="_blank">탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 62 |                      | <a href="http://boj.kr/5014" target="_blank">스타트링크</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 63 |                      | <a href="http://boj.kr/2589" target="_blank">보물섬</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 64 |                      | <a href="http://boj.kr/9019" target="_blank">DSLR</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 65 |                      | <a href="http://boj.kr/11559" target="_blank">Puyo Puyo</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 66 |                      | <a href="http://boj.kr/12851" target="_blank">숨바꼭질 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 67 |                      | <a href="http://boj.kr/17141" target="_blank">연구소 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 68 |                      | <a href="http://boj.kr/17129" target="_blank">윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 69 |                      | <a href="http://boj.kr/16174" target="_blank">점프왕 쩰리 (Large)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 70 |                      | <a href="http://boj.kr/2194" target="_blank">유닛 이동시키기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 71 |                      | <a href="http://boj.kr/16432" target="_blank">떡장수와 호랑이</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 72 |                      | <a href="http://boj.kr/1707" target="_blank">이분 그래프</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 73 |                      | <a href="http://boj.kr/17142" target="_blank">연구소 3</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 74 |                      | <a href="http://boj.kr/5427" target="_blank">불</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 75 |                      | <a href="http://boj.kr/13913" target="_blank">숨바꼭질 4</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 76 |                      | <a href="http://boj.kr/2638" target="_blank">치즈</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 77 |                      | <a href="http://boj.kr/2665" target="_blank">미로만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 78 |                      | <a href="http://boj.kr/1726" target="_blank">로봇</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 79 |                      | <a href="http://boj.kr/2234" target="_blank">성곽</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 80 |                      | <a href="http://boj.kr/6087" target="_blank">레이저 통신</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 81 |                      | <a href="http://boj.kr/2151" target="_blank">거울 설치</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 82 |                      | <a href="http://boj.kr/14923" target="_blank">미로 탈출</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 83 |                      | <a href="http://boj.kr/2146" target="_blank">다리 만들기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 84 |                      | <a href="http://boj.kr/14442" target="_blank">벽 부수고 이동하기 2</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 85 |                      | <a href="http://boj.kr/10711" target="_blank">모래성</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 86 |                      | <a href="http://boj.kr/16947" target="_blank">서울 지하철 2호선</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 87 |                      | <a href="http://boj.kr/16988" target="_blank">Baaaaaaaaaduk2 (Easy)</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 88 |                      | <a href="http://boj.kr/16985" target="_blank">Maaaaaaaaaze</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 89 |                      | <a href="http://boj.kr/17616" target="_blank">등수 찾기</a> | <img height="25px" width="25px=" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
