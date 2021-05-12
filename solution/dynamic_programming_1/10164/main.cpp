// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/17e87614b6d540ca996295b147a740d5
#include<bits/stdc++.h>

using namespace std;

int N, M, K;
int DP[22][22];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> K;
    int y = N, x = M;
    if(K > 0) {
        --K;
        y = K / M + 1, x = K % M + 1; // 1 - based
    }
    DP[1][1] = 1;
    for(int i=1;i<=y; i++) {
        for(int j=1;j<=x;j++) {
            if(i == 1 && j == 1) continue;
            DP[i][j] = DP[i][j - 1] + DP[i - 1][j];
        }
    }
    for(int i=y;i<=N;i++){
        for(int j=x;j<=M;j++){
            if(i == y && j == x) continue;
            DP[i][j] = DP[i][j - 1] + DP[i - 1][j];
        }
    }
    cout << DP[N][M];

    return 0;
}
