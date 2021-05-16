// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/0bfccc47735a40d5a6cb460a341ef24e
#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> G;
vector<int> isRoot, depth, parent;
int N, root;

void input() {
    cin >> N;
    G = vector<vector<int>>(N + 1);
    isRoot = vector<int>(N + 1, 1);
    depth = vector<int>(N + 1);
    parent = vector<int>(N + 1);
    for(int i = 1; i < N; i++) {
        int par, child; cin >> par >> child;
        G[par].push_back(child);
        G[child].push_back(par);
        isRoot[child] = 0;
    }
    for(int i = 1; i < N; i++) {
        if(isRoot[i] == 1) root = i;
    }
}

void dfs(int cur, int prev, int dep) {
    depth[cur] = dep;
    for(auto &nxt: G[cur]) {
        if(nxt == prev) continue;
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

    int T; cin >> T;
    while(T--) {
        input();
        dfs(root, -1, 0);
        int u, v; cin >> u >> v;
        cout << getLCA(u, v) << '\n';
    }

    return 0;
}
