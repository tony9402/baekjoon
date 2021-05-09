// author    : seastar105
// Co-author : 
// Link      : http://boj.kr/dc1ee586858242998fd86a247e4754bf
#include<bits/stdc++.h>
using namespace std;
int N, M;
vector<vector<int>> G(100005);
bool vis[100005];
int comp_cnt;

void dfs(int cur) {
  vis[cur] = true;
  ++comp_cnt;
  for(const int &nxt : G[cur]) {
    if(!vis[nxt]) dfs(nxt);
  }
}

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  cin >> N >> M;
  for(int i=0;i<M;++i) {
    // u v가 주어지면 u가 해킹됐을 때 u도 해킹된다.
    int u, v; cin >> u >> v;
    G[v].push_back(u);
  }
  vector<int> ans;
  int max_cnt = -1;
  // 각 정점에서 DFS 혹은 BFS를 진행해서 도달 가능한 정점 수가 제일 많은 것을 고른다.
  for(int i=1;i<=N;++i) {
    memset(vis, false, N+1);
    comp_cnt = 0;
    dfs(i);
    if(max_cnt < comp_cnt) {
      max_cnt = comp_cnt;
      ans.clear();
      ans.push_back(i);
    }
    else if(max_cnt == comp_cnt) ans.push_back(i);
  }
  for(const int &x : ans) cout << x << ' ';
  cout << '\n';
  return 0;
}
