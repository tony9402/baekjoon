// author    : seastar105
// Co-author : 
// Link      : http://boj.kr/fb5956759f34490582dc6dfb806ec546
#include<bits/stdc++.h>
using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int N, M;
char board[105][105];
int dist[105][105];

bool valid(int x, int y) {
  return 0<=x && x<N && 0<=y && y<M;
}

int main() {
  cin.tie(nullptr); ios::sync_with_stdio(false);
  cin >> N >> M;
  for(int i=0;i<N;++i) cin >> board[i];
  // 최단거리를 구해야하기 때문에 DFS는 안 됩니다.
  memset(dist, -1, sizeof(dist));
  queue<pair<int,int>> q;
  q.push({0, 0});
  dist[0][0] = 1;
  while(!q.empty()) {
    pair<int,int> p = q.front();
    int x = p.first;
    int y = p.second;
    q.pop();
    for(int i=0;i<4;++i) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(!valid(nx, ny)) continue;        // out of bound
      if(board[nx][ny] == '0') continue;  // blocked
      if(dist[nx][ny] != -1) continue;    // already visited
      dist[nx][ny] = dist[x][y] + 1;
      q.push({nx, ny});
    }
  }
  cout << dist[N-1][M-1] << '\n';
  return 0;
}
