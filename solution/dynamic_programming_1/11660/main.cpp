// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c28a9148cd334f45b6edcbc40ae7ec15
#include<bits/stdc++.h>

using namespace std;

int arr[1033][1033], dp[1033][1033];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q; cin >> N >> Q;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=N;j++) {
            cin >> arr[i][j];
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j];
        }
    }

    for(int i=0;i<Q;i++) {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        cout << dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1] << '\n';
    }

    return 0;
}
