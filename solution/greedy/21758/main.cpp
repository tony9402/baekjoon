// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ba24cf477f634be3b516d7475296bf67
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

const int MAXN = 100000;
ll arr[MAXN + 5], prefix[MAXN + 5];

ll psum(int l, int r) {
    return prefix[r] - prefix[l - 1];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
        prefix[i] = prefix[i - 1] + arr[i];
    }

    ll answer = 0;
    for(int i = 2; i < N; i++ ){
        answer = max(answer, psum(2, i) + psum(i, N - 1));
        answer = max(answer, psum(2, N) + psum(i + 1, N) - arr[i]);
        answer = max(answer, psum(1, N - 1) + psum(1, i - 1) - arr[i]);
    }
    cout << answer;

    return 0;
}
