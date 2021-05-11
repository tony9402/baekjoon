// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/18fb3fd9e39e4f0eb7cb530d83a16848
#include<bits/stdc++.h>

using namespace std;

int uf[40404];

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
    for(int i=0;i<=N;i++)uf[i] = -1;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++) {
            int x;cin >> x;
            if(x) merge(i, j);
        }
    }
    int pre; cin >> pre;
    bool answer = true;
    for(int i=1;i<M;i++){
        int cur; cin >> cur;
        if(find(pre) != find(cur)) answer = false;
        pre = cur;
    }
    if(answer) cout << "YES";
    else cout << "NO";

    return 0;
}
