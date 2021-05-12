// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/4e4a00d9c5004014aab885f379b3578f
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
int uf[1005];

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

    int N; cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            ll x;cin >> x;
            if(i >= j)continue;
            v.emplace_back(x, i, j);
        }
    }
    sort(v.begin(), v.end());
    
    ll ans = 0;
    for(int i=0;i<(int)v.size();i++){
        if(merge(v[i].a, v[i].b)) ans += v[i].w;
    }
    cout << ans;

    return 0;
}

