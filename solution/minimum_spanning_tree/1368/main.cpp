// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/4d85f4e6945642d4abb30eb188480027
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int uf[303];

int find(int x) {
    if(uf[x] < 0) return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if(a == b)return false;
    uf[b] = a;
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    vector<tuple<ll, int, int>> w;
    for(int i=0;i<=N;i++) uf[i] = -1;
    for(int i=0;i<N;i++) {
        int x;cin >> x;
        w.emplace_back(x, i, N);
    }
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            int x; cin >> x;
            if(i >= j) continue;
            w.emplace_back(x, i, j);
        }
    }

    sort(w.begin(), w.end());
    ll answer = 0;
    for(auto &[W, a, b]: w) {
        if(merge(a, b)) answer += W;
    }
    cout << answer;

    return 0;
}
