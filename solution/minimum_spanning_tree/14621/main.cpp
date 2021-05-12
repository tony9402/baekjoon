// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a20ee766193d402682304dd53ce97459
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

struct Node{
    ll w;
    int a, b;
    Node(ll w=0, int a=0, int b=0):w(w),a(a),b(b){}
    bool operator<(const Node& o) const { return w < o.w; }
};
vector<Node> v;
int uf[1005], group[1005];

int find(int x) {
    if(uf[x] < 0)return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b){
    a = find(a);
    b = find(b);
    if(a == b)return false;
    uf[b] = a;
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    // Initial 
    for(int i=0;i<1005;i++) uf[i] = -1;

    int N, M; cin >> N >> M;
    for(int i=1;i<=N;i++) {
        char x;cin >> x;
        group[i] = x == 'M';
    }
    for(int i=0;i<M;i++){
        int a, b, c; cin >> a >> b >> c;
        if(group[a] == group[b])continue;
        v.emplace_back(c, a, b);
    }
    sort(v.begin(), v.end());
    
    ll ans = 0;
    for(int i=0;i<(int)v.size();i++){
        if(merge(v[i].a, v[i].b)) ans += v[i].w;
    }
    for(int i=1;i<=N;i++) {
        if(find(1) != find(i)) ans = -1;
    }
    cout << ans;

    return 0;
}

