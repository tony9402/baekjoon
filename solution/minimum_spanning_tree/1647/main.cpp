// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c11a8cc3ac094764bf7e1131ad9939ac
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

constexpr int MAXN = 100005;
int uf[MAXN];

int find(int x) {
    if(uf[x] < 0)return x;
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
    
    vector<tuple<int, int, int>> w;
    for(int i=0;i<MAXN;i++) uf[i] = -1;
    
    int N, M; cin >> N >> M;
    for(int i=0;i<M;i++) {
        int a, b, c; cin >> a >> b >> c;
        w.emplace_back(c, a, b);
    }
    sort(w.begin(), w.end());
    
    ll ans = 0;
    int cnt = 0;
    for(auto &[c, a, b]: w) {
        if(merge(a, b)) {
            ans += c;
            if(++cnt == N - 2) break;
        }
    }
    cout << ans;

    return 0;
}

