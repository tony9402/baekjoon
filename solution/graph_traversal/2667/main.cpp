// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/64816e87e7c24254ae15748732036df3
#include <bits/stdc++.h>
using namespace std;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int N;
string board[30];
bool vis[30][30];

bool valid(int x, int y) {
    return 0 <= x && x < N && 0 <= y && y < N;
}

int bfs(int src_x, int src_y) {
    queue<pair<int,int>> q;
    vis[src_x][src_y] = true;
    q.push({src_x, src_y});
    int ret = 0;
    while(!q.empty()) {
        pair<int,int> p = q.front();
        int x = p.first;
        int y = p.second;
        ++ret;
        q.pop();
        for(int i=0;i<4;++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(!valid(nx, ny)) continue;
            if(vis[nx][ny]) continue;
            if(board[nx][ny] == '0') continue;
            vis[nx][ny] = true;
            q.push({nx, ny});
        }
    }
    return ret;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> board[i];
    vector<int> ans;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (vis[i][j]) continue;
            if (board[i][j] == '0') continue;
            // BFS start
            int cnt = bfs(i, j);
            ans.push_back(cnt);
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for (int x : ans) cout << x << '\n';
    return 0;
}
