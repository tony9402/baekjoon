// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/1b2b0b0081d042e2a24298d188de8ba1
#include <bits/stdc++.h>
using namespace std;
int N, M;
vector<vector<int>> G(100005);
bool vis[100005];
int comp_cnt;

void dfs(int cur) {
    vis[cur] = true;
    ++comp_cnt;
    for (const int &nxt : G[cur]) {
        if (!vis[nxt]) dfs(nxt);
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N >> M;
    for (int i = 0; i < M; ++i) {
        // u v가 주어지면 v가 해킹됐을 때 u도 해킹된다.
        int u, v;
        cin >> u >> v;
        G[v].push_back(u);
    }
    vector<int> ans;
    int max_cnt = -1;
    for (int i = 1; i <= N; ++i) {
        memset(vis, false, N + 1);
        comp_cnt = 0;
        dfs(i);
        if (max_cnt < comp_cnt) {
            max_cnt = comp_cnt;
            ans.clear();
            ans.push_back(i);
        }
        else if (max_cnt == comp_cnt) ans.push_back(i);
    }
    for (const int &x : ans) cout << x << ' ';
    cout << '\n';
    return 0;
}
