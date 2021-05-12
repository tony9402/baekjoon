// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/4a2e9c2a7d9a44e7b0c4eda2c2cae10b
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll DP[33][33];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T; cin >> T;
    DP[0][0] = 1;
    for(int i=1;i<=30;i++) {
        DP[i][0] = 1;
        for(int j=1;j<=30;j++) {
            DP[i][j] = DP[i - 1][j] + DP[i - 1][j - 1];
        }
    }
    while(T--) {
        int N, M; cin >> N >> M;
        cout << DP[M][N] << '\n';
    }

    return 0;
}
