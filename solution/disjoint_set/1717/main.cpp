// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/681761d952b14fd58d55c93eaf11c0ef
#include<bits/stdc++.h>

using namespace std;

int uf[1000005];

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

    int N, M; cin >> N >> M;
    for(int i=0;i<=N;i++) uf[i] = -1;
    for(int i=0;i<M;i++) {
        int t, a, b; cin >> t >> a >> b;
        if(t == 1) {
            if(find(a) == find(b)) cout << "YES\n";
            else cout << "NO\n";
        }
        else merge(a, b);
    }

    return 0;
}
