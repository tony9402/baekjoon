//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/12a5a69bad604f3dbd054c028b3e2994

#include <bits/stdc++.h>

using namespace std;

int num[100010], sum[100010];

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);

    int N, M; cin >> N >> M;

    // 입력과 동시에 누적합을 구해놓습니다.
    for(int i = 1;i <= N;i++) {
        cin >> num[i];
        sum[i] = sum[i - 1] + num[i];
    }

    // end까지의 합 - begin전 까지의 합 = begin ~ end사이 합
    for(int i = 0;i < M;i++) {
        int begin, end;
        cin >> begin >> end;
        cout << sum[end] - sum[begin - 1] << '\n';
    }

    return 0;
} 
