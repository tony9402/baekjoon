// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/06e81c4ff5a74105a074835a38318b13
#include<bits/stdc++.h>
using namespace std;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int a[10][10];
bool vis[10][10];
int N, M;
vector<pair<int,int>> empty_cell;
int ans;

bool valid(int x, int y) {
    return 0<=x && x<N && 0<=y && y<M;
}

void dfs(int idx, int cnt) {
    if(cnt == 3) {
        queue<pair<int,int>> q;
        memset(vis, false, sizeof(vis));
        for(int i=0;i<N;++i) {
            for(int j=0;j<M;++j) {
                if(!vis[i][j] && a[i][j] == 2) {
                    queue<pair<int,int>> q;
                    q.push({i, j});
                    vis[i][j] = true;
                    while(!q.empty()) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        for(int k=0;k<4;++k) {
                            int nx = x + dx[k];
                            int ny = y + dy[k];
                            if(!valid(nx, ny) || vis[nx][ny]) continue;
                            if(a[nx][ny] == 1) continue;
                            vis[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                }
            }
        }
        int safe = 0;
        for(int i=0;i<N;++i) {
            for(int j=0;j<M;++j) {
                if(!vis[i][j] && a[i][j] == 0) ++safe;
            }
        }
        ans = max(ans, safe);
        return ;
    }
    if(idx == empty_cell.size()) return ;
    int x = empty_cell[idx].first;
    int y = empty_cell[idx].second;
    a[x][y] = 1;
    dfs(idx+1, cnt+1);
    a[x][y] = 0;
    dfs(idx+1, cnt);
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> N >> M;
    for(int i=0;i<N;++i) {
        for(int j=0;j<M;++j) {
            cin >> a[i][j];
            if(a[i][j] == 0) empty_cell.emplace_back(i, j);
        }
    }
    dfs(0, 0);
    cout << ans << '\n';
    return 0;
}
