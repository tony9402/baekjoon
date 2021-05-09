// author    : seastar105
// Co-author : 
// Link      : http://boj.kr/fd8bb8e57e6447159c15c2847457e3b1
#include<bits/stdc++.h>
using namespace std;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int N;
char board[30][30];
bool vis[30][30];
// DFS로도 풀 수 있습니다.
bool valid(int x, int y) {
  return 0<=x && x<N && 0<=y && y<N;
}

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  cin >> N;
  for(int i=0;i<N;++i) cin >> board[i];
  vector<int> ans;
  for(int i=0;i<N;++i) {
    for(int j=0;j<N;++j) {
      if(vis[i][j]) continue;
      if(board[i][j] == '0') continue;
      // BFS start
      queue<pair<int,int>> q;
      vis[i][j] = true;
      q.push({i, j});
      int cnt = 0;
      while(!q.empty()) {
        pair<int,int> p = q.front();
        int x = p.first;
        int y = p.second;
        ++cnt;
        q.pop();
        for(int k=0;k<4;++k) {
          int nx = x + dx[k];
          int ny = y + dy[k];
          if(!valid(nx, ny)) continue;
          if(vis[nx][ny]) continue;
          if(board[nx][ny] == '0') continue;
          vis[nx][ny] = true;
          q.push({nx, ny});
        }
      }
      ans.push_back(cnt);
    }
  }
  sort(ans.begin(), ans.end());
  cout << ans.size() << '\n';
  for(int x : ans) cout << x << '\n';
  return 0;
}
