# Shortest Path (최단거리)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

최단거리 문제를 해결할 때 사용하는 알고리즘 중 다익스트라, 벨만-포드, 플로이드 위주로 뽑았습니다.

문제를 읽어보고 문제를 해결하기 위해 필요한 무엇인지 생각해봐야 합니다.

위 알고리즘들의 차이와 각 알고리즘의 특성을 이해하지 못한 상황에서 문제를 푸는 것은 도움이 안된다고 생각합니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7273)


|순번|추천 문제|문제 번호|문제 이름|난이도|풀이 링크|
|:--:|:--:|:--:|:--:|:--:|:--:|
|000|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/18352" target="_blank">18352</a>|<a href="https://www.acmicpc.net/problem/18352" target="_blank">특정 거리의 도시 찾기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/>||
|001|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/11403" target="_blank">11403</a>|<a href="https://www.acmicpc.net/problem/11403" target="_blank">경로 찾기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>||
|002|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/13549" target="_blank">13549</a>|<a href="https://www.acmicpc.net/problem/13549" target="_blank">숨바꼭질 3</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|003|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/11657" target="_blank">11657</a>|<a href="https://www.acmicpc.net/problem/11657" target="_blank">타임머신</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|004|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1753" target="_blank">1753</a>|<a href="https://www.acmicpc.net/problem/1753" target="_blank">최단경로</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|005|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1277" target="_blank">1277</a>|<a href="https://www.acmicpc.net/problem/1277" target="_blank">발전소 설치</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|006|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/2224" target="_blank">2224</a>|<a href="https://www.acmicpc.net/problem/2224" target="_blank">명제 증명</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|007|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1956" target="_blank">1956</a>|<a href="https://www.acmicpc.net/problem/1956" target="_blank">운동</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|008|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/22865" target="_blank">22865</a>|<a href="https://www.acmicpc.net/problem/22865" target="_blank">가장 먼 곳</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|009|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/11404" target="_blank">11404</a>|<a href="https://www.acmicpc.net/problem/11404" target="_blank">플로이드</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|010|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/14938" target="_blank">14938</a>|<a href="https://www.acmicpc.net/problem/14938" target="_blank">서강그라운드</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|011|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/11265" target="_blank">11265</a>|<a href="https://www.acmicpc.net/problem/11265" target="_blank">끝나지 않는 파티</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|012|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/10159" target="_blank">10159</a>|<a href="https://www.acmicpc.net/problem/10159" target="_blank">저울</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|013|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1865" target="_blank">1865</a>|<a href="https://www.acmicpc.net/problem/1865" target="_blank">웜홀</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|014|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1613" target="_blank">1613</a>|<a href="https://www.acmicpc.net/problem/1613" target="_blank">역사</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|015|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1238" target="_blank">1238</a>|<a href="https://www.acmicpc.net/problem/1238" target="_blank">파티</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|016|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1719" target="_blank">1719</a>|<a href="https://www.acmicpc.net/problem/1719" target="_blank">택배</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>|<a href="./../../solution/shortest_path/1719" target="_blank">바로 가기</a>|
|017|:heavy_check_mark:|<a href="https://www.acmicpc.net/problem/1507" target="_blank">1507</a>|<a href="https://www.acmicpc.net/problem/1507" target="_blank">궁금한 민호</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|018||<a href="https://www.acmicpc.net/problem/1058" target="_blank">1058</a>|<a href="https://www.acmicpc.net/problem/1058" target="_blank">친구</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/>||
|019||<a href="https://www.acmicpc.net/problem/18243" target="_blank">18243</a>|<a href="https://www.acmicpc.net/problem/18243" target="_blank">Small World Network</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>||
|020||<a href="https://www.acmicpc.net/problem/1389" target="_blank">1389</a>|<a href="https://www.acmicpc.net/problem/1389" target="_blank">케빈 베이컨의 6단계 법칙</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>||
|021||<a href="https://www.acmicpc.net/problem/1446" target="_blank">1446</a>|<a href="https://www.acmicpc.net/problem/1446" target="_blank">지름길</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>||
|022||<a href="https://www.acmicpc.net/problem/15723" target="_blank">15723</a>|<a href="https://www.acmicpc.net/problem/15723" target="_blank">n단 논법</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>||
|023||<a href="https://www.acmicpc.net/problem/17396" target="_blank">17396</a>|<a href="https://www.acmicpc.net/problem/17396" target="_blank">백도어</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|024||<a href="https://www.acmicpc.net/problem/1916" target="_blank">1916</a>|<a href="https://www.acmicpc.net/problem/1916" target="_blank">최소비용 구하기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|025||<a href="https://www.acmicpc.net/problem/20168" target="_blank">20168</a>|<a href="https://www.acmicpc.net/problem/20168" target="_blank">골목 대장 호석 - 기능성</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|026||<a href="https://www.acmicpc.net/problem/9205" target="_blank">9205</a>|<a href="https://www.acmicpc.net/problem/9205" target="_blank">맥주 마시면서 걸어가기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|027||<a href="https://www.acmicpc.net/problem/2660" target="_blank">2660</a>|<a href="https://www.acmicpc.net/problem/2660" target="_blank">회장뽑기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|028||<a href="https://www.acmicpc.net/problem/5972" target="_blank">5972</a>|<a href="https://www.acmicpc.net/problem/5972" target="_blank">택배 배송</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|029||<a href="https://www.acmicpc.net/problem/14284" target="_blank">14284</a>|<a href="https://www.acmicpc.net/problem/14284" target="_blank">간선 이어가기 2</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>||
|030||<a href="https://www.acmicpc.net/problem/1504" target="_blank">1504</a>|<a href="https://www.acmicpc.net/problem/1504" target="_blank">특정한 최단 경로</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|031||<a href="https://www.acmicpc.net/problem/20007" target="_blank">20007</a>|<a href="https://www.acmicpc.net/problem/20007" target="_blank">떡 돌리기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|032||<a href="https://www.acmicpc.net/problem/10282" target="_blank">10282</a>|<a href="https://www.acmicpc.net/problem/10282" target="_blank">해킹</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|<a href="./../../solution/shortest_path/10282" target="_blank">바로 가기</a>|
|033||<a href="https://www.acmicpc.net/problem/1261" target="_blank">1261</a>|<a href="https://www.acmicpc.net/problem/1261" target="_blank">알고스팟</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|034||<a href="https://www.acmicpc.net/problem/21940" target="_blank">21940</a>|<a href="https://www.acmicpc.net/problem/21940" target="_blank">가운데에서 만나기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|035||<a href="https://www.acmicpc.net/problem/4485" target="_blank">4485</a>|<a href="https://www.acmicpc.net/problem/4485" target="_blank">녹색 옷 입은 애가 젤다지?</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|036||<a href="https://www.acmicpc.net/problem/18223" target="_blank">18223</a>|<a href="https://www.acmicpc.net/problem/18223" target="_blank">민준이와 마산 그리고 건우</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|037||<a href="https://www.acmicpc.net/problem/13424" target="_blank">13424</a>|<a href="https://www.acmicpc.net/problem/13424" target="_blank">비밀 모임</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|038||<a href="https://www.acmicpc.net/problem/2458" target="_blank">2458</a>|<a href="https://www.acmicpc.net/problem/2458" target="_blank">키 순서</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>||
|039||<a href="https://www.acmicpc.net/problem/20182" target="_blank">20182</a>|<a href="https://www.acmicpc.net/problem/20182" target="_blank">골목 대장 호석 - 효율성 1</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|040||<a href="https://www.acmicpc.net/problem/11779" target="_blank">11779</a>|<a href="https://www.acmicpc.net/problem/11779" target="_blank">최소비용 구하기 2</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|041||<a href="https://www.acmicpc.net/problem/11562" target="_blank">11562</a>|<a href="https://www.acmicpc.net/problem/11562" target="_blank">백양로 브레이크</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/>||
|042||<a href="https://www.acmicpc.net/problem/20183" target="_blank">20183</a>|<a href="https://www.acmicpc.net/problem/20183" target="_blank">골목 대장 호석 - 효율성 2</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|043||<a href="https://www.acmicpc.net/problem/9370" target="_blank">9370</a>|<a href="https://www.acmicpc.net/problem/9370" target="_blank">미확인 도착지</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|044||<a href="https://www.acmicpc.net/problem/13911" target="_blank">13911</a>|<a href="https://www.acmicpc.net/problem/13911" target="_blank">집 구하기</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|045||<a href="https://www.acmicpc.net/problem/1445" target="_blank">1445</a>|<a href="https://www.acmicpc.net/problem/1445" target="_blank">일요일 아침의 데이트</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|046||<a href="https://www.acmicpc.net/problem/11780" target="_blank">11780</a>|<a href="https://www.acmicpc.net/problem/11780" target="_blank">플로이드 2</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|047||<a href="https://www.acmicpc.net/problem/2982" target="_blank">2982</a>|<a href="https://www.acmicpc.net/problem/2982" target="_blank">국왕의 방문</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|048||<a href="https://www.acmicpc.net/problem/2211" target="_blank">2211</a>|<a href="https://www.acmicpc.net/problem/2211" target="_blank">네트워크 복구</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/>||
|049||<a href="https://www.acmicpc.net/problem/16118" target="_blank">16118</a>|<a href="https://www.acmicpc.net/problem/16118" target="_blank">달빛 여우</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/>||
|050||<a href="https://www.acmicpc.net/problem/2307" target="_blank">2307</a>|<a href="https://www.acmicpc.net/problem/2307" target="_blank">도로검문</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/>||
|051||<a href="https://www.acmicpc.net/problem/1219" target="_blank">1219</a>|<a href="https://www.acmicpc.net/problem/1219" target="_blank">오민식의 고민</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/>||
|052||<a href="https://www.acmicpc.net/problem/22870" target="_blank">22870</a>|<a href="https://www.acmicpc.net/problem/22870" target="_blank">산책 (large)</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/17.svg"/>||