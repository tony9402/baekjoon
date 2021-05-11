// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/038f38ed8c6f41149b051350cb3cabd1
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<int> V(N), DP(N);
    for(auto &i: V) cin >> i;
    for(int i=0;i<N;i++) {
        DP[i] = V[i];
        for(int j=0;j<i;j++) {
            if(V[i] > V[j]) {
                DP[i] = max(DP[i], DP[j] + V[i]);
            }
        }
    }
    cout << *max_element(DP.begin(), DP.end());

    return 0;
}
