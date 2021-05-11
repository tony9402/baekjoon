// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/4ff69fc575384408beee739a7904de45
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    vector<vector<int>> DP(N + 1, vector<int>(M + 1));
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            int x; cin >> x;
            DP[i][j] = max({DP[i-1][j], DP[i][j-1], DP[i-1][j-1]}) + x;
        }
    }
    cout << DP[N][M];

    return 0;
}
