// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/b4aa5eb711ac44259b6e1d3b8a03ca59
#include<bits/stdc++.h>

using namespace std;

const int dy[] = {1,0,-1,0};
const int dx[] = {0,1,0,-1};
int arr[333][333];
bool used[333][333], used2[333][333];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M, R; cin >> N >> M >> R;
    for(int i=0;i<N;i++) for(int j=0;j<M;j++) cin >> arr[i][j];

    for(int i=0;i<N;i++){
        int y = i, x = i, dir = 0;
        vector<int> cur;
        cur.push_back(arr[y][x]);
        used[y][x] = true;
        while(dir < 4){
            int qy = y + dy[dir];
            int qx = x + dx[dir];
            if(0 > qy || qy >= N || 0 > qx || qx >= M || used[qy][qx]){
                dir++;
                continue;
            }
            y = qy, x = qx;
            used[y][x] = true;
            cur.push_back(arr[y][x]);
        }
        int L = cur.size();
        int idx = (L - R % L) % L;
        y = i, x = i, dir = 0;
        used2[y][x] = true;
        arr[y][x] = cur[idx];
        if(++idx == (int)cur.size()) idx = 0;
        while(dir < 4){
            int qy = y + dy[dir];
            int qx = x + dx[dir];
            if(0 > qy || qy >= N || 0 > qx || qx >= M || used2[qy][qx]){
                dir++;
                continue;
            }
            y = qy, x = qx;
            used2[y][x] = true;
            arr[y][x] = cur[idx];
            if(++idx == (int)cur.size()) idx = 0;
        }
    }
    for(int i=0;i<N;i++) {
        for(int j=0;j<M;j++){
            cout << arr[i][j] << " ";
        }
        cout << '\n';
    }

    return 0;
}
