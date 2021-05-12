// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ecf2284ada79472da95d933e310ca959
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<int> V(N);
    for(auto &i: V) cin >> i;
    sort(V.begin(), V.end());
    int Q; cin >> Q;
    for(int i=0;i<Q;i++) {
        int x;cin >> x;
        if(binary_search(V.begin(), V.end(), x)) cout << 1 << '\n';
        else cout << 0 << '\n';
    }

    return 0;
}
