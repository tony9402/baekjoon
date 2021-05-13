// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/98893b9366134af9a87bd3a182b912ca
#include<bits/stdc++.h>
using namespace std;
int W, H;
int a[105][105];
bool vis[105][105];
int dy[2][6] = {
    {-1, 0, 1, 1, 0, -1},
    {-1, 0, 1, 1, 0, -1}
};  // 세로
int dx[2][6] = {
    {0, 1, 0, -1, -1, -1},
    {1, 1, 1, 0, -1, 0}
};  // 가로

bool valid(int y, int x) {
    return 0<=y && y<=H+1 && 0<=x && x<=W+1;
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> W >> H;
    for(int i=1;i<=H;++i) for(int j=1;j<=W;++j) cin >> a[i][j];
    // flood fill from outside with white
    queue<pair<int,int>> q;
    vis[0][0] = true;
    q.emplace(0, 0);
    while(!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for(int i=0;i<6;++i) {
            int ny = y + dy[y%2][i];
            int nx = x + dx[y%2][i];
            if(!valid(ny, nx)) continue;
            if(vis[ny][nx] || a[ny][nx]) continue;
            vis[ny][nx] = true;
            q.emplace(ny, nx);
        }
    }
    // count adjacent edge between filled region for each black node
    int ans = 0;
    for(int y=1;y<=H;++y) {
        for(int x=1;x<=W;++x) {
            if(a[y][x] == 0) continue;
            for(int i=0;i<6;++i) {
                int ny = y + dy[y%2][i];
                int nx = x + dx[y%2][i];
                if(vis[ny][nx]) ++ans;
            }
        }
    }
    cout << ans << '\n';
    return 0;
}
