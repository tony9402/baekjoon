## 업데이트 로그

뽑아야 하는 문제가 많고 이를 보기 좋게 표로 정리하는 과정은 너무 노가다성이 많기 때문에 편하게 작업할 수 있도록 업데이트 하고 있습니다.

<details>
    <summary>자세히</summary><p>

 - 2021.04.28
   - [오늘의 문제](https://github.com/tony9402/baekjoon/blob/main/picked.md) 뽑히는 문제 난이도 변경 
     - 이전 난이도
       - 1번 브론즈 5 ~ 실버 1
       - 2번 골드 5 ~ 골드 3
       - 3번 골드 5 ~ 골드 3
       - 4번 골드 2 ~ 골드 1
     - 변경된 난이도
       - 1번 브론즈 5 ~ 실버 3
       - 2번 실버 2 ~ 골드 4
       - 3번 실버 2 ~ 골드 4
       - 4번 골드 3 ~ 골드 1
 - 2021.04.22 ~ 2021.04.23
   - 코드 리팩토링 일부 완료
     - 나머지는 시간 날때마다 하나씩 할 예정
   - 문제 뽑는 방식 변경
     - 이전 방식에서 [새로운](https://raw.githubusercontent.com/tony9402/baekjoon/main/dynamic_programming_2/list.md) 방식으로 변경
     - 이전 방식 : [추천 문제 여부],[문제 이름],[문제 번호],[난이도],[솔루션 링크]
     - 새로운 방식 : [추천 문제 여부],[문제 번호],[솔루션 링크]
   - 매일 새벽에 자동으로 문제 뽑는 스크립트 제작 및 기능 추가
     - [Solved.ac](https://solved.ac/) 기준 브론즈 5 ~ 골드 1 사이인 문제가 4문제 일정 조건 안에서 랜덤하게 뽑음
     - [오늘 문제](https://github.com/tony9402/baekjoon/blob/main/picked.md) 형식으로 업데이트.
     - [문제 뽑는 스크립트](https://github.com/tony9402/baekjoon/blob/main/scripts/pick_problem.cpp)
   - [Contributors](https://github.com/tony9402/baekjoon#contributors) 정보 만드는 표 스크립트 제작
     - Contributor 정보만 [여기](https://github.com/tony9402/baekjoon/blob/main/markdown/contributor.json)에 넣으면 자동으로 표를 생성

 - 2021.04.20
   - [tree](./tree) 태그 추가
     - 트리와 관련된 문제 뽑았습니다.
   - [Contributors](https://github.com/tony9402/baekjoon#contributors) 디자인을 변경하였습니다.
   - [문제집](https://www.acmicpc.net/workbook/by/tony9402) 전체를 업데이트 하였습니다.
   - 각 문제집에 문제 번호를 볼 수 있도록 추가하였고 문제 번호로도 백준으로 이동할 수 있도록 업데이트 했습니다.

 - 2021.04.03
   - [discussions](https://github.com/tony9402/baekjoon/discussions) 추가

 - 2021.04.02
   - [README.md](https://github.com/tony9402/baekjoon/blob/main/README.md) 자동 생성 스크립트 제작
     - 각 알고리즘 문제는 자동으로 추가되고 [status.md](https://github.com/tony9402/baekjoon/blob/main/status.md)에 자동으로 카운팅되지만 README.md에서는 안되는 현상 발견하여 해결
   - 알고리즘 문제 제목 틀린거 자동으로 찾아 수정
   - 일정 주기마다 알고리즘 난이도 갱신
   - 문제 정보를 담는 json을 만듦

 - 2021.03.31
   - [Github Actions](https://github.com/tony9402/baekjoon/actions) 도입
   - [solved](http://solved.ac)의 난이도 변경을 일정 시간마다 체크하여 자동 업데이트 (백준 문제집은 X)
   - 난이도 변경은 [로그](https://github.com/tony9402/baekjoon/blob/main/change_level.log)로 남겨놓음
   - 솔루션 파일만 폴더 형식에만 맞추면 알아서 README 업데이트(솔루션 링크 연결 등)
 
 - 2021.03.27
   - README.md 업데이트를 더더욱 자동화를 위해 README.md 위에 설명 부분을 header.md로 분리

 - 2021.03.15 
   - 추천 문제 [solution](https://github.com/tony9402/baekjoon/tree/main/solution) (C++ 기준) 완성도 정리하는 스크립트 생성

 - 2021.01.15
   - 문제 [이렇게](https://raw.githubusercontent.com/tony9402/baekjoon/main/math/list.md) 뽑으면 자동으로 markdown 테이블을 만들어주는 스크립트 제작

</p></details>


