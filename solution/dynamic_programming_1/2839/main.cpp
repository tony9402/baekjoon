// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/48cb7b8049444c7eb5cdc5752dd5eb66
#include <bits/stdc++.h>

using namespace std;

int DP[5005];

int main(){
    ios::sync_with_stdio(false); 
    cin.tie(0);
    
    const int INF = 50000;
    for(int i=1;i<=5000;i++) DP[i] = INF;
    DP[3] = 1; 

    for(int i=5;i<=5000;i++) DP[i] = min({ DP[i], DP[i - 3] + 1, DP[i - 5] + 1});
        
    int N; cin >> N;
    if(DP[N] == INF)DP[N] = -1;
    cout << DP[N];
}
