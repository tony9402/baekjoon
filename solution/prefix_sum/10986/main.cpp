// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/20743d7ff7ab44a3b917f45b8e064f16
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll mod[1000]; // 0 ~ 999

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    ll sum =0;
    mod[0] = 1;
    for(int i=1;i<=N;i++) {
        int x; cin >> x;
        x %= M;
        sum = (sum + x) % M;
        mod[sum] ++;
    }
    ll answer = 0;
    for(int i=0;i<M;i++) {
        answer += mod[i] * (mod[i] - 1) / 2;
    }
    cout << answer;

    return 0;
}
