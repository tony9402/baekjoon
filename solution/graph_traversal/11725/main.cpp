// author    : seastar105
// Co-author : 
// Link      : http://boj.kr/822762feeccc440a8781623d1bed2bb6
#include<bits/stdc++.h>
using namespace std;
int N;
vector<vector<int>> G(100005);
int parent[100005];

// 주어진 그래프가 트리이기 때문에 부모 노드로만 올라가지 않으면 
// 각 노드를 한번씩 방문하는 것이 보장됩니다.
void dfs(int cur) {
  for(const int &nxt : G[cur]) {
    if(parent[cur] == nxt) continue;
    parent[nxt] = cur;
    dfs(nxt);
  }
}

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  cin >> N;
  for(int i=0;i<N-1;++i) {
    int u, v; cin >> u >> v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  dfs(1);
  for(int i=2;i<=N;++i) cout << parent[i] << '\n';
  return 0;
}
