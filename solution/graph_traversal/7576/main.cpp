// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/b632f242053b45c4bc98739905f01d18
#include<bits/stdc++.h>
using namespace std;
int N, M;
int arr[1005][1005];
int dist[1005][1005];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

bool valid(int x, int y) {
    return 0<=x && x<N && 0<=y && y<M;
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> M >> N;
    int tot = 0, done = 0;
    for(int i=0;i<N;++i) {
        for(int j=0;j<M;++j) {
            cin >> arr[i][j];
            if(arr[i][j] >= 0) ++tot;
            if(arr[i][j] == 1) ++done;
        }
    }
    if(tot == done) {
        cout << 0 << '\n';
        return 0;
    }
    memset(dist, -1, sizeof(dist));
    queue<pair<int,int>> q;
    for(int i=0;i<N;++i) {
        for(int j=0;j<M;++j) {
            if(arr[i][j] == 1) {
                dist[i][j] = 0;
                q.emplace(i, j);
            }
        }
    }
    int ans = 0;
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        ans = max(ans, dist[x][y]);
        for(int i=0;i<4;++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(!valid(nx, ny)) continue;
            if(arr[nx][ny] == -1 || dist[nx][ny] != -1) continue;
            dist[nx][ny] = dist[x][y]+1;
            ++done;
            q.emplace(nx, ny);
        }
    }
    if(tot == done) cout << ans << '\n';
    else cout << -1 << '\n';
    return 0;
}
