// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/7a6068ec74014cc68c29b63fd59c25ea
#include<bits/stdc++.h>

using namespace std;

const int MAXN = 1000005;
int uf[MAXN], cnt[MAXN];

int find(int x) {
    if(uf[x] < 0) return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if(a == b)return false;
    uf[b] = a;
    cnt[a] += cnt[b];
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<MAXN;i++) {
        uf[i] = -1;
        cnt[i] = 1;
    }
    for(int i=0;i<N;i++) {
        char cmd; cin >> cmd;
        if(cmd == 'I') {
            int a, b; cin >> a >> b;
            merge(a, b);
        }
        else {
            int a; cin >> a;
            cout << cnt[find(a)] << '\n';
        }
    }

    return 0;
}
