// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/8c3a1dd56b2b4bb6ba312c9dbd6eff0d
#include<bits/stdc++.h>

using namespace std;

int N, M, T;
const int dy[] = {-1,1,0,0}; // UDLR
const int dx[] = {0,0,-1,1};
const int UP[] = {0,3,1,2};
const int DOWN[] = {1,3,0,2};

vector<vector<int>> Map;
vector<int> Y;
bool inrange(int y, int x) { return 0 <= y && y < N && 0 <= x && x < M; }

void input(){ 
    cin >> N >> M >> T;
    Map = vector<vector<int>>(N, vector<int>(M));
    for(int i=0;i<N;i++) {
        for(int j=0;j<M;j++){
            cin >> Map[i][j];
            if(Map[i][j] == -1) {
                Map[i][j] = 0;
                Y.push_back(i);
            }
        }
    }
}

void spread() {
    vector<vector<int>> tmp = Map;
    for(int i=0;i<N;i++) {
        for(int j=0;j<M;j++) {
            if(tmp[i][j] == 0) continue;
            int div = tmp[i][j] / 5;
            for(int k=0;k<4;k++) {
                int qy = i + dy[k];
                int qx = j + dx[k];
                if((qy == Y[0] || qy == Y[1]) && qx == 0) continue;
                if(inrange(qy, qx)) {
                    Map[i][j] -= div;
                    Map[qy][qx] += div;
                }
            }
        }
    }
}

void air() {
    vector<vector<int>> used(N, vector<int>(M));
    int y = Y[0];
    int x = 0;
    int dir = 0;
    while(dir < 4) {
        Map[Y[0]][0] = 0;
        int nexty = y + dy[UP[dir]];
        int nextx = x + dx[UP[dir]];
        if(0 <= nexty && nexty <= Y[0] && 0 <= nextx && nextx < M && used[nexty][nextx] == 0) {
            used[nexty][nextx] = 1;
            Map[y][x] = Map[nexty][nextx];
            y = nexty;
            x = nextx;
        }
        else dir ++;
    }
    y = Y[1];
    x = 0;
    dir = 0;
    while(dir < 4) {
        Map[Y[1]][0] = 0;
        int nexty = y + dy[DOWN[dir]];
        int nextx = x + dx[DOWN[dir]];
        if(Y[1] <= nexty && nexty < N && 0 <= nextx && nextx < M && used[nexty][nextx] == 0) {
            used[nexty][nextx] = 1;
            Map[y][x] = Map[nexty][nextx];
            y = nexty;
            x = nextx;
        }
        else dir ++;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    input();
    while(T--){
        spread();
        air();
    }
    int answer = 0;
    for(int i=0;i<N;i++) for(int j=0;j<M;j++) answer += Map[i][j];
    cout << answer;

    return 0;
}
