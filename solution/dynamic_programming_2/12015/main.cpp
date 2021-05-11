// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c74669b0329d4d59ad5145504275e7ac
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<int> V(N), DP;
    for(auto &i: V) cin >> i;
    for(int i=0;i<N;i++) {
        auto it = lower_bound(DP.begin(), DP.end(), V[i]);
        if(it == DP.end()) DP.push_back(V[i]);
        else *it = V[i];
    }
    cout << (int)DP.size();

    return 0;
}
