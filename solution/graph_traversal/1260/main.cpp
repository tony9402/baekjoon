// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/1b2b0b0081d042e2a24298d188de8ba1
#include <bits/stdc++.h>
using namespace std;
int N, M, V;
vector<vector<int>> G(1005);
vector<int> dfs_order, bfs_order;
bool vis[1005];

void dfs(int cur) {
    vis[cur] = true;
    dfs_order.push_back(cur);
    for (const int &nxt : G[cur]) {
        if (!vis[nxt])
            dfs(nxt);
    }
}

void bfs(int src) {
    queue<int> q;
    vis[src] = true;
    q.push(src);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        bfs_order.push_back(cur);
        for (const int &nxt : G[cur]) {
            if (!vis[nxt]) {
                vis[nxt] = true;
                q.push(nxt);
            }
        }
    }
}

int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N >> M >> V;
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    // 번호가 더 빠른 정점을 방문하기 위해서 인접 리스트를 정점 번호순으로 정렬
    for (int i = 1; i <= N; ++i) sort(G[i].begin(), G[i].end());
    memset(vis, false, sizeof(vis));
    dfs(V);
    memset(vis, false, sizeof(vis));
    bfs(V);
    for (const int &x : dfs_order) cout << x << ' ';
    cout << '\n';
    for (const int &x : bfs_order) cout << x << ' ';
    cout << '\n';
    return 0;
}
