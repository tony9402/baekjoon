//Authored by : suin8
//Co-authored by : tony9402
//Link : http://boj.kr/bf868d6487744424a792c188673bf339

#include <bits/stdc++.h>

using namespace std;

int num[200010], cnt[100010];

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);

    int N, K; cin >> N >> K;

    for(int i = 1;i <= N;i++)
        cin >> num[i];

    // start와 end사이에 겹치는 수가 K개 이하일 때는 end를 늘리며
    // 최대 길이를 늘리고
    // K개 초과일 때는 begin를 늘리며 겹치는 수가 빠질때까지 begin을 증가
    int ans = 0;
    for(int begin = 1, end = 1; begin <= N; begin ++) {
        while(end <= N && cnt[num[end]] < K) ++cnt[num[end++]];
        ans = max(ans, end - begin);
        cnt[num[begin]]--;
    }

    cout << ans;

    return 0;
}
