// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/421ce6bb00ca40709c15dc5df958d5f1
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

const int MAXN = 100000;
ll prefix[MAXN + 5];
ll L[MAXN + 5], R[MAXN + 5];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=1;i<=N;i++) {
        cin >> prefix[i];
        prefix[i] += prefix[i - 1];
    }

    for(int i = 1; i <= N; i++) {
        L[i] = L[i - 1];
        if(prefix[N] == 4 * prefix[i]) L[i] ++;
    }

    for(int i = N - 1; i >= 1; i--) {
        R[i] = R[i + 1];
        if(prefix[N] * 3 == 4 * prefix[i]) R[i] ++;
    }

    ll answer = 0;
    for(int i = 2; i < N - 1; i++) {
        if(prefix[N] == prefix[i] * 2) answer += L[i - 1] * R[i + 1];
    }
    cout << answer;

    return 0;
}
