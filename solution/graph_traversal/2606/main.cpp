// author    : seastar105
// co-author : 
// Link      : http://boj.kr/475842c947c542f1b8a7aa540031059a
#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> G(105);
bool vis[105];
int N, M;

void dfs(int cur) {
  vis[cur] = true;
  for(const int &nxt : G[cur]) {
    if(!vis[nxt]) dfs(nxt);
  }
}

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  cin >> N >> M;
  for(int i=0;i<M;++i) {
    int u, v; cin >> u >> v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  dfs(1);
  int ans = 0;
  for(int i=1;i<=N;++i) ans += vis[i];
  cout << ans-1 << '\n';  // except vertex 1
  return 0;
}
0 comments on commit 2f55c0c
