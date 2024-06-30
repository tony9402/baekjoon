# Minimum Spanning Tree (최소 스패닝 트리)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

최소 스패닝 트리 문제를 뽑아봤습니다.

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7175)


|순번|추천 문제|문제 번호|문제 이름|난이도|풀이 링크|
|:--:|:--:|:--:|:--:|:--:|:--:|
|000|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1197" target="_blank">1197</a>|<a href="https://www.acmicpc.net/problem/1197" target="_blank">최소 스패닝 트리</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/1197" target="_blank">바로 가기</a>|
|001|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/21924" target="_blank">21924</a>|<a href="https://www.acmicpc.net/problem/21924" target="_blank">도시 건설</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/21924" target="_blank">바로 가기</a>|
|002|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/16398" target="_blank">16398</a>|<a href="https://www.acmicpc.net/problem/16398" target="_blank">행성 연결</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/16398" target="_blank">바로 가기</a>|
|003|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1647" target="_blank">1647</a>|<a href="https://www.acmicpc.net/problem/1647" target="_blank">도시 분할 계획</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/1647" target="_blank">바로 가기</a>|
|004|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1922" target="_blank">1922</a>|<a href="https://www.acmicpc.net/problem/1922" target="_blank">네트워크 연결</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/1922" target="_blank">바로 가기</a>|
|005|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1774" target="_blank">1774</a>|<a href="https://www.acmicpc.net/problem/1774" target="_blank">우주신과의 교감</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>|<a href="./../solution/minimum_spanning_tree/1774" target="_blank">바로 가기</a>|
|006|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/14621" target="_blank">14621</a>|<a href="https://www.acmicpc.net/problem/14621" target="_blank">나만 안되는 연애</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>|<a href="./../solution/minimum_spanning_tree/14621" target="_blank">바로 가기</a>|
|007|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1368" target="_blank">1368</a>|<a href="https://www.acmicpc.net/problem/1368" target="_blank">물대기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>|<a href="./../solution/minimum_spanning_tree/1368" target="_blank">바로 가기</a>|
|008||<a href="https://www.acmicpc.net/problem/13905" target="_blank">13905</a>|<a href="https://www.acmicpc.net/problem/13905" target="_blank">세부</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|009||<a href="https://www.acmicpc.net/problem/6497" target="_blank">6497</a>|<a href="https://www.acmicpc.net/problem/6497" target="_blank">전력난</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../solution/minimum_spanning_tree/6497" target="_blank">바로 가기</a>|
|010||<a href="https://www.acmicpc.net/problem/18769" target="_blank">18769</a>|<a href="https://www.acmicpc.net/problem/18769" target="_blank">그리드 네트워크</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|011||<a href="https://www.acmicpc.net/problem/14950" target="_blank">14950</a>|<a href="https://www.acmicpc.net/problem/14950" target="_blank">정복자</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|012||<a href="https://www.acmicpc.net/problem/17490" target="_blank">17490</a>|<a href="https://www.acmicpc.net/problem/17490" target="_blank">일감호에 다리 놓기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|013||<a href="https://www.acmicpc.net/problem/13418" target="_blank">13418</a>|<a href="https://www.acmicpc.net/problem/13418" target="_blank">학교 탐방하기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|014||<a href="https://www.acmicpc.net/problem/2406" target="_blank">2406</a>|<a href="https://www.acmicpc.net/problem/2406" target="_blank">안정적인 네트워크</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|015||<a href="https://www.acmicpc.net/problem/1414" target="_blank">1414</a>|<a href="https://www.acmicpc.net/problem/1414" target="_blank">불우이웃돕기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|016||<a href="https://www.acmicpc.net/problem/4386" target="_blank">4386</a>|<a href="https://www.acmicpc.net/problem/4386" target="_blank">별자리 만들기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>|<a href="./../solution/minimum_spanning_tree/4386" target="_blank">바로 가기</a>|
|017||<a href="https://www.acmicpc.net/problem/16202" target="_blank">16202</a>|<a href="https://www.acmicpc.net/problem/16202" target="_blank">MST 게임</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|018||<a href="https://www.acmicpc.net/problem/10423" target="_blank">10423</a>|<a href="https://www.acmicpc.net/problem/10423" target="_blank">전기가 부족해</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|019||<a href="https://www.acmicpc.net/problem/20010" target="_blank">20010</a>|<a href="https://www.acmicpc.net/problem/20010" target="_blank">악덕 영주 혜유</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>|<a href="./../solution/minimum_spanning_tree/20010" target="_blank">바로 가기</a>|
|020||<a href="https://www.acmicpc.net/problem/1944" target="_blank">1944</a>|<a href="https://www.acmicpc.net/problem/1944" target="_blank">복제 로봇</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/>||
|021||<a href="https://www.acmicpc.net/problem/1045" target="_blank">1045</a>|<a href="https://www.acmicpc.net/problem/1045" target="_blank">도로</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/>||
|022||<a href="https://www.acmicpc.net/problem/17472" target="_blank">17472</a>|<a href="https://www.acmicpc.net/problem/17472" target="_blank">다리 만들기 2</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/>||
|023||<a href="https://www.acmicpc.net/problem/2887" target="_blank">2887</a>|<a href="https://www.acmicpc.net/problem/2887" target="_blank">행성 터널</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/>|<a href="./../solution/minimum_spanning_tree/2887" target="_blank">바로 가기</a>|