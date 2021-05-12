// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/80903be26b2e47eeb98b990db8689c5b
#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
vector<int> depth, parent;

void dfs(int cur = 1, int par = -1, int dep = 0) {
    depth[cur] = dep;
    for(auto &nxt: graph[cur]) {
        if(nxt == par) continue;
        parent[nxt] = cur;
        dfs(nxt, cur, dep + 1);
    }
}

int getLCA(int a, int b) {
    if(depth[a] > depth[b]) swap(a, b);
    while(depth[a] < depth[b]) b = parent[b];
    while(a != b) {
        a = parent[a];
        b = parent[b];
    }
    return a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    graph.resize(N + 1);
    parent.resize(N + 1);
    depth.resize(N + 1);
    for(int i = 1; i < N; i++) {
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    dfs();

    int Q; cin >> Q;
    while(Q--){
        int a, b; cin >> a >> b;
        cout << getLCA(a, b) << '\n';
    }

    return 0;
}
