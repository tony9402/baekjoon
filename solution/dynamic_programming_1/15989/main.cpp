// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/7363aaeb37fd489aaa5c0ad142ce8a7a
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll DP[10005][4];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    for(int i=1;i<=3;i++) {
        for(int j=1;j<=i;j++) {
            DP[i][j] = 1;
        }
    }

    for(int i=4;i<=10000;i++) {
        for(int j=1;j<=3;j++) {
            for(int k=1;k<=j;k++) {
                DP[i][j] += DP[i - j][k];
            }
        }
    }
    
    int T; cin >> T;
    while(T--){ 
        int n; cin >> n;
        ll answer = 0;
        for(int i=1;i<=3;i++) answer += DP[n][i];
        cout << answer << '\n';
    }

    return 0;
}
