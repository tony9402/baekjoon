// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/acc4b75def8e48d995163a01bcc23068
#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
vector<int> siz;

void dfs(int cur, int prv) {
    siz[cur] = 1;

    for(auto &nxt: graph[cur]) {
        if(nxt == prv) continue;
        dfs(nxt, cur);
        siz[cur] += siz[nxt];
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, R, Q; cin >> N >> R >> Q;
    graph.resize(N + 1);
    siz.resize(N + 1);
    for(int i=1;i<N;i++) {
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(R, R);
    
    while(Q--) {
        int x;cin >> x;
        cout << siz[x] << '\n';
    }

    return 0;
}
