// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/2d250c49804d4fb6a38cbe6e752cd87d
#include<bits/stdc++.h>

using namespace std;

int prefix[5050], sleep[5050], used[5050];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K, Q, M; cin >> N >> K >> Q >> M;
    for(int i=1;i<=K;i++) {
        int x;cin >> x;
        sleep[x] = 1;
    }
    for(int i=1;i<=Q;i++) {
        int x;cin >> x;
        if(sleep[x]) continue;
        for(int j=x;j<=N+2;j+=x) {
            if(sleep[j]) continue;
            used[j] = 1;
        }
    }

    for(int i=3;i<=N+2;i++) {
        prefix[i] = prefix[i-1];
        if(used[i] == 0) prefix[i] ++;
    }

    for(int i=1;i<=M;i++){
        int L, R; cin >> L >> R;
        cout << prefix[R] - prefix[L - 1] << '\n';
     }

    return 0;
}
