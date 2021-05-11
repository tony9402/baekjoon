// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/f4a2942a69264111a18e39d0c384209e
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> G(105);
bool vis[105];
int N, M;

void dfs(int cur) {
    vis[cur] = true;
    for (const int &nxt : G[cur]) {
        if (!vis[nxt]) dfs(nxt);
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N >> M;
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    dfs(1);
    int ans = 0;
    for (int i = 1; i <= N; ++i) ans += vis[i];
    cout << ans - 1 << '\n'; // except vertex 1
    return 0;
}
