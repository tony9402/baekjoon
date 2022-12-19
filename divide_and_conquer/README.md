# Divide and conquer (분할정복)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7275)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2630" target="_blank">2630</a> | <a href="https://www.acmicpc.net/problem/2630" target="_blank">색종이 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | <a href="./../solution/divide_and_conquer/2630">바로가기</a> |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17829" target="_blank">17829</a> | <a href="https://www.acmicpc.net/problem/17829" target="_blank">222-풀링</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | <a href="./../solution/divide_and_conquer/17829">바로가기</a> |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18222" target="_blank">18222</a> | <a href="https://www.acmicpc.net/problem/18222" target="_blank">투에-모스 문자열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | <a href="./../solution/divide_and_conquer/18222">바로가기</a> |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1992" target="_blank">1992</a> | <a href="https://www.acmicpc.net/problem/1992" target="_blank">쿼드트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/divide_and_conquer/1992">바로가기</a> |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1074" target="_blank">1074</a> | <a href="https://www.acmicpc.net/problem/1074" target="_blank">Z</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/divide_and_conquer/1074">바로가기</a> |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2447" target="_blank">2447</a> | <a href="https://www.acmicpc.net/problem/2447" target="_blank">별 찍기 - 10</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/divide_and_conquer/2447">바로가기</a> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2448" target="_blank">2448</a> | <a href="https://www.acmicpc.net/problem/2448" target="_blank">별 찍기 - 11</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/divide_and_conquer/2448">바로가기</a> |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/4256" target="_blank">4256</a> | <a href="https://www.acmicpc.net/problem/4256" target="_blank">트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/divide_and_conquer/4256">바로가기</a> |
| 08 |                      | <a href="https://www.acmicpc.net/problem/4779" target="_blank">4779</a> | <a href="https://www.acmicpc.net/problem/4779" target="_blank">칸토어 집합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/divide_and_conquer/4779">바로가기</a> |
| 09 |                      | <a href="https://www.acmicpc.net/problem/1780" target="_blank">1780</a> | <a href="https://www.acmicpc.net/problem/1780" target="_blank">종이의 개수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 10 |                      | <a href="https://www.acmicpc.net/problem/1802" target="_blank">1802</a> | <a href="https://www.acmicpc.net/problem/1802" target="_blank">종이 접기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/divide_and_conquer/1802">바로가기</a> |
| 11 |                      | <a href="https://www.acmicpc.net/problem/14600" target="_blank">14600</a> | <a href="https://www.acmicpc.net/problem/14600" target="_blank">샤워실 바닥 깔기 (Small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 12 |                      | <a href="https://www.acmicpc.net/problem/5904" target="_blank">5904</a> | <a href="https://www.acmicpc.net/problem/5904" target="_blank">Moo 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 13 |                      | <a href="https://www.acmicpc.net/problem/2374" target="_blank">2374</a> | <a href="https://www.acmicpc.net/problem/2374" target="_blank">같은 수로 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 14 |                      | <a href="https://www.acmicpc.net/problem/1493" target="_blank">1493</a> | <a href="https://www.acmicpc.net/problem/1493" target="_blank">박스 채우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 15 |                      | <a href="https://www.acmicpc.net/problem/1030" target="_blank">1030</a> | <a href="https://www.acmicpc.net/problem/1030" target="_blank">프렉탈 평면</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 16 |                      | <a href="https://www.acmicpc.net/problem/16438" target="_blank">16438</a> | <a href="https://www.acmicpc.net/problem/16438" target="_blank">원숭이 스포츠</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 17 |                      | <a href="https://www.acmicpc.net/problem/14601" target="_blank">14601</a> | <a href="https://www.acmicpc.net/problem/14601" target="_blank">샤워실 바닥 깔기 (Large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/> |                      |
