# Disjoint Set (분리집합)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

일반적으로 분리집합을 표현하는데에는 배열을 활용한 유니언 파인드 자료구조를 사용합니다.

다만, 카카오 기출 문제에서 일반적인 유니언 파인드 구조를 사용하지 못하도록 전체 크기를 엄청나게 늘린 문제가 출제 되었던 만큼,
배열이 아닌 해시나 이진트리를 활용해 유니언 파인드 구조를 만들어 보는 연습도 필요합니다!

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/6784)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1717" target="_blank">1717</a> | <a href="https://www.acmicpc.net/problem/1717" target="_blank">집합의 표현</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1717">바로가기</a> |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1976" target="_blank">1976</a> | <a href="https://www.acmicpc.net/problem/1976" target="_blank">여행 가자</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1976">바로가기</a> |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16562" target="_blank">16562</a> | <a href="https://www.acmicpc.net/problem/16562" target="_blank">친구비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/16562">바로가기</a> |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18116" target="_blank">18116</a> | <a href="https://www.acmicpc.net/problem/18116" target="_blank">로봇 조립</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/18116">바로가기</a> |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/4195" target="_blank">4195</a> | <a href="https://www.acmicpc.net/problem/4195" target="_blank">친구 네트워크</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/disjoint_set/4195">바로가기</a> |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10775" target="_blank">10775</a> | <a href="https://www.acmicpc.net/problem/10775" target="_blank">공항</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/disjoint_set/10775">바로가기</a> |
| 06 |                      | <a href="https://www.acmicpc.net/problem/17352" target="_blank">17352</a> | <a href="https://www.acmicpc.net/problem/17352" target="_blank">여러분의 다리가 되어 드리겠습니다!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/disjoint_set/17352">바로가기</a> |
| 07 |                      | <a href="https://www.acmicpc.net/problem/7511" target="_blank">7511</a> | <a href="https://www.acmicpc.net/problem/7511" target="_blank">소셜 네트워킹 어플리케이션</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 08 |                      | <a href="https://www.acmicpc.net/problem/20040" target="_blank">20040</a> | <a href="https://www.acmicpc.net/problem/20040" target="_blank">사이클 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 09 |                      | <a href="https://www.acmicpc.net/problem/12893" target="_blank">12893</a> | <a href="https://www.acmicpc.net/problem/12893" target="_blank">적의 적</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 10 |                      | <a href="https://www.acmicpc.net/problem/1043" target="_blank">1043</a> | <a href="https://www.acmicpc.net/problem/1043" target="_blank">거짓말</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1043">바로가기</a> |
| 11 |                      | <a href="https://www.acmicpc.net/problem/16168" target="_blank">16168</a> | <a href="https://www.acmicpc.net/problem/16168" target="_blank">퍼레이드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 12 |                      | <a href="https://www.acmicpc.net/problem/20955" target="_blank">20955</a> | <a href="https://www.acmicpc.net/problem/20955" target="_blank">민서의 응급 수술</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 13 |                      | <a href="https://www.acmicpc.net/problem/15789" target="_blank">15789</a> | <a href="https://www.acmicpc.net/problem/15789" target="_blank">CTP 왕국은 한솔 왕국을 이길 수 있을까?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 14 |                      | <a href="https://www.acmicpc.net/problem/11085" target="_blank">11085</a> | <a href="https://www.acmicpc.net/problem/11085" target="_blank">군사 이동</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 15 |                      | <a href="https://www.acmicpc.net/problem/17090" target="_blank">17090</a> | <a href="https://www.acmicpc.net/problem/17090" target="_blank">미로 탈출하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 16 |                      | <a href="https://www.acmicpc.net/problem/16724" target="_blank">16724</a> | <a href="https://www.acmicpc.net/problem/16724" target="_blank">피리 부는 사나이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 17 |                      | <a href="https://www.acmicpc.net/problem/14595" target="_blank">14595</a> | <a href="https://www.acmicpc.net/problem/14595" target="_blank">동방 프로젝트 (Large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 18 |                      | <a href="https://www.acmicpc.net/problem/3108" target="_blank">3108</a> | <a href="https://www.acmicpc.net/problem/3108" target="_blank">로고</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 19 |                      | <a href="https://www.acmicpc.net/problem/17398" target="_blank">17398</a> | <a href="https://www.acmicpc.net/problem/17398" target="_blank">통신망 분할</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
