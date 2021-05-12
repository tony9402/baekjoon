// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/5182387e6c9745238986dcbe9231c45d
#include<bits/stdc++.h>

using namespace std;
int prefix[303][303];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            cin >> prefix[i][j];
            prefix[i][j] = prefix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1];
        }
    }
    int Q; cin >> Q;
    while(Q--) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        --a; -- b;
        cout << prefix[c][d] - prefix[a][d] - prefix[c][b] + prefix[a][b] << '\n';
    }

    return 0;
}
