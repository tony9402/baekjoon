// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/03ac57850f3e4b83b42d8300cccc91fb
#include<bits/stdc++.h>

using namespace std;

constexpr int MAXN = 200005;
int uf[MAXN], siz[MAXN];

int find(int x) {
    if(uf[x] < 0) return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a); b = find(b);
    if(a == b)return false;
    uf[b] = a;
    siz[a] += siz[b];
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        for(int i=0;i<MAXN;i++) {
            uf[i] = -1;
            siz[i] = 1;
        }
        int n; cin >> n;
        unordered_map<string, int> mp;
        int idx = 0;
        
        for(int i=0;i<n;i++){
            string a, b; cin >> a >> b;
            if(mp.count(a) == 0) mp[a] = idx++;
            if(mp.count(b) == 0) mp[b] = idx++;
            merge(mp[a], mp[b]);
            cout << siz[find(mp[a])] << '\n';
        }
    }

    return 0;
}
