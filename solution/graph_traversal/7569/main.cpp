// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/391fb64958a448c8afc7082bb219b4af
#include<bits/stdc++.h>
using namespace std;
int N, M, H;
int dx[6] = {-1,1,0,0,0,0};
int dy[6] = {0,0,-1,1,0,0};
int dz[6] = {0,0,0,0,-1,1};
int arr[105][105][105];
int dist[105][105][105];

struct Node {
    int x, y, z;
    Node() {};
    Node(int x_, int y_, int z_) : x(x_), y(y_), z(z_) {};
};

bool valid(int x, int y, int z) {
    return 0<=x && x<H && 0<=y && y<N && 0<=z && z<M;
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> M >> N >> H;
    int tot = 0, done = 0;
    for(int i=0;i<H;++i) {
        for(int j=0;j<N;++j) {
            for(int k=0;k<M;++k) {
                cin >> arr[i][j][k];
                if(arr[i][j][k] >= 0) ++tot;
                if(arr[i][j][k] == 1) ++done;
            }
        }
    }
    if(done == tot) {
        cout << 0 << '\n';
        return 0;
    }
    memset(dist, -1, sizeof(dist));
    queue<Node> q;
    for(int i=0;i<H;++i) {
        for(int j=0;j<N;++j) {
            for(int k=0;k<M;++k) {
                if(arr[i][j][k] == 1) {
                    q.emplace(i, j, k);
                    dist[i][j][k] = 0;
                }
            }
        }
    }
    int ans = 0;
    while(!q.empty()) {
        int x = q.front().x;
        int y = q.front().y;
        int z = q.front().z;
        q.pop();
        ans = max(ans, dist[x][y][z]);
        for(int i=0;i<6;++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            int nz = z + dz[i];
            if(!valid(nx, ny, nz)) continue;
            if(arr[nx][ny][nz] == -1 || dist[nx][ny][nz] != -1) continue;
            dist[nx][ny][nz] = dist[x][y][z] + 1;
            ++done;
            q.emplace(nx, ny, nz);
        }
    }
    if(tot != done) cout << -1 << '\n';
    else cout << ans << '\n';
    return 0;
}
