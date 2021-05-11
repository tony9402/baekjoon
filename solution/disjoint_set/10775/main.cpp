// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/f71cbcd7b21940189fe6db7f99852f09
#include<bits/stdc++.h>

using namespace std;

constexpr int MAXN = 100005;
int uf[MAXN];

int find(int x) {
    if(uf[x] < 0) return x;
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

    int N, M; cin >> N >> M;
    for(int i=0;i<=N;i++) uf[i] = -1;
    int answer = 0;
    for(int i=0;i<M;i++){
        int x;cin >> x;
        int cur = find(x);
        if(cur == 0) break;
        merge(cur - 1, cur);
        answer ++;
    }
    cout << answer;

    return 0;
}
