// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/56c86c3089dd42369ddf2d2277479675
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int uf[1005];

int find(int x) {
    if(uf[x] < 0) return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if(a == b) return false;
    uf[b] = a;
    return true;
}

vector<pair<int, int>> v;
vector<tuple<ll, int, int>> w;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=0;i<N;i++) {
        int a, b; cin >> a >> b;
        v.emplace_back(a, b);

        uf[i] = -1;
    }
    for(int i=0;i<M;i++) {
        int a, b; cin >> a >> b;
        merge(--a, --b);
    }

    for(int i=0;i<N;i++) {
        for(int j=i+1;j<N;j++) {
           ll f = v[i].first - v[j].first;
           ll s = v[i].second - v[j].second;
           w.emplace_back(f*f+s*s,i,j);
        }
    }

    sort(w.begin(), w.end());

    double answer = 0.;
    for(auto &[W, a, b]: w) {
        if(merge(a, b)) answer += sqrt(W);
    }

    cout << setprecision(2) << fixed << answer;

    return 0;
}
