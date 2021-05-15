// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ae5c8a4d54074ca1a2af053ecbad14a1
#include<bits/stdc++.h>

using namespace std;

const int INF = 0x3f3f3f3f;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<vector<int>> V(N, vector<int>(N));
    vector<vector<int>> DP(N, vector<int>(N, INF));
    DP[0][0]=0;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            cin >> V[i][j];
            if(j > 0){
                int d = max(0, V[i][j] - V[i][j-1] + 1);
                DP[i][j]=min(DP[i][j], DP[i][j-1] + d);
            }
            if(i > 0){
                int d = max(0, V[i][j] - V[i-1][j] + 1);
                DP[i][j] = min(DP[i][j], DP[i-1][j] + d);
            }
        }
    }
    cout << DP[N-1][N-1];

    return 0;
}
