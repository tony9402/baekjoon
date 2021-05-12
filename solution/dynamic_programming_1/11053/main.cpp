// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/67f06494af394db6958644f6cb20e8fe
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<int> V(N), DP(N);
    for(auto &i: V) cin >> i;
    for(int i=0;i<N;i++) {
        DP[i] = 1;
        for(int j=0;j<i;j++) {
            if(V[i] > V[j]) {
                DP[i] = max(DP[i], DP[j] + 1);
            }
        }
    }
    cout << *max_element(DP.begin(), DP.end());

    return 0;
}
