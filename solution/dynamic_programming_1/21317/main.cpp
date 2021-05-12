// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/7b74ffa836cb49029ffc4ee08767c9db
#include<bits/stdc++.h>

using namespace std;

int DP[105][2], arr[105][2];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=1;i<N;i++) cin >> arr[i][0] >> arr[i][1];
    int k; cin >> k;
    for(int i=2;i<105;i++) DP[i][0] = DP[i][1] = INT_MAX;
    for(int i=1;i<N;i++) {
        DP[i + 1][0] = min(DP[i + 1][0], DP[i][0] + arr[i][0]);
        DP[i + 1][1] = min(DP[i + 1][1], DP[i][1] + arr[i][0]);
        DP[i + 2][0] = min(DP[i + 2][0], DP[i][0] + arr[i][1]);
        DP[i + 2][1] = min(DP[i + 2][1], DP[i][1] + arr[i][1]);
        DP[i + 3][1] = min(DP[i + 3][1], DP[i][0] + k);
    }
    cout << min(DP[N][0], DP[N][1]);

    return 0;
}
