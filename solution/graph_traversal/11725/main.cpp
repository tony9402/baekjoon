// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/c28e084e8adc4eb78851cc603e7f5b37
#include <bits/stdc++.h>
using namespace std;
int N;
vector<vector<int>> G(100005);
int parent[100005];

void dfs(int cur) {
    for (const int &nxt : G[cur]) {
        if (parent[cur] == nxt) continue;
        parent[nxt] = cur;
        dfs(nxt);
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N;
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    dfs(1);
    for (int i = 2; i <= N; ++i) cout << parent[i] << '\n';
    return 0;
}
