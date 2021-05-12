// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/7a8607af45e042df9e44b48962548e1a
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll DP[100005][4];
const ll MOD = 1e9 + 9;
const int MAXN = 100000;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    for(int i=1;i<=3;i++) DP[i][i] = DP[3][i] = 1;
    for(int i=4;i<=MAXN;i++){
        for(int j=1;j<=3;j++){
            for(int k=1;k<=3;k++){
                if(j == k)continue;
                DP[i][j] = (DP[i][j] + DP[i - j][k]) % MOD;
            }
        }
    }
    int T; cin >> T;
    while(T--){
        int n; cin >> n;
        cout << (DP[n][1] + DP[n][2] + DP[n][3]) % MOD << '\n';
    }
    return 0;
}
