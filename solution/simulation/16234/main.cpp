#include<bits/stdc++.h>

using namespace std;

queue<pair<int, int>> Q;
const int dy[] = {-1, 1, 0, 0};
const int dx[] = { 0, 0,-1, 1};
int Map[55][55], N, L, R;
bool used[55][55];

void BFS(int a, int b) {
    if(used[a][b]) return;
    int total = 0, cnt = 0;
    vector<pair<int, int>> path;
    queue <pair<int, int>> q;
    q.emplace(a, b);
    used[a][b] = true;
    while(!q.empty()) {
        auto [y, x] = q.front(); q.pop();
        total += Map[y][x];
        cnt   ++;
        path.emplace_back(y, x);

        for(int k=0;k<4;k++) {
            int qy = y + dy[k];
            int qx = x + dx[k];
            if(0 > qy || qy >= N || 0 > qx || qx >= N)continue;
            if(used[qy][qx]) continue;
            int value = abs(Map[qy][qx] - Map[y][x]);
            if(L > value || value > R) continue;
            used[qy][qx] = true;
            q.emplace(qy, qx);
        }
    }
    if(cnt < 2) return;
    for(auto &[y, x]: path) {
        Map[y][x] = total / cnt;
        Q.emplace(y, x);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> L >> R;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            cin >> Map[i][j];
            Q.emplace(i, j);
        }
    }

    int answer = -1;
    while(!Q.empty()) {
        for(int i=0;i<N;i++) {
            for(int j=0;j<N;j++) {
                used[i][j] = false;
            }
        }

        int qsize = Q.size();
        answer ++;
        for(int i = 0; i < qsize; i++) {
            auto [y, x] = Q.front(); Q.pop();
            BFS(y, x);
        }
    }
    cout << answer;

    return 0;
}
