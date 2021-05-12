// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/22b0ae85671b4e3fb5561ef97c4b4b74
#include<bits/stdc++.h>

using namespace std;

struct Board {
    int N, M;
    vector<vector<int>> Map;
    Board(int _N=10, int _M=4) : N(_N), M(_M), Map(_N, vector<int>(_M)) { }
    bool isrange(int y, int x) { return 0 <= y && y < N && 0 <= x && x < M; } 
    void put(int type, int x, int y) {
        Map[x][y] = 1;
        if(type == 2) Map[x][y + 1] = 1;
        else if(type == 3) Map[x + 1][y] = 1;

        while(true) {
            if(type == 1) {
                int nx = x + 1;
                int ny = y;
                if(!isrange(nx, ny)) break;
                if(Map[nx][ny] == 1) break;
                Map[nx][ny] = Map[x][y];
                Map[x][y] = 0;
                x ++;
            }
            else if(type == 2) {
                int nx1 = x + 1;
                int ny1 = y;
                int nx2 = x + 1;
                int ny2 = y + 1;
                if(!isrange(nx1, ny1) || !isrange(nx2, ny2)) break;
                if(Map[nx1][ny1] == 1 || Map[nx2][ny2] == 1) break;
                Map[nx1][ny1] = Map[x][ny1];
                Map[nx2][ny2] = Map[x][ny2];
                Map[x][ny1] = Map[x][ny2] = 0;
                x ++;
            }
            else { 
                int nx1 = x + 1;
                int ny1 = y;
                int nx2 = x + 2;
                int ny2 = y;
                if(!isrange(nx1, ny1) || !isrange(nx2, ny2)) break;
                if(Map[nx2][ny2] == 1) break;
                Map[nx2][ny2] = Map[x + 1][ny1];
                Map[nx1][ny1] = Map[x][ny1];
                Map[x][ny1] = 0;
                x++;
            }
        }
    }
    int checkLine() {
        int score = 0;
        for(int i=N-1;i>=0;) {
            bool line = true;
            for(int j=0;j<M;j++) {
                if(Map[i][j] == 0) line = false;
            }
            if(!line) {
                i--; 
                continue;
            }
            score ++;
            for(int L=i;L>0;L--) {
                for(int j=0;j<M;j++) {
                    Map[L][j] = Map[L - 1][j];
                }
            }
            for(int j=0;j<M;j++) Map[0][j] = 0;
        }
        return score;
    }
    void eraseLine() {
        while(true) {
            bool hasLine = false;
            for(int i=4;!hasLine && i<=5;i++) {
                for(int j=0;!hasLine && j<M;j++) {
                    if(Map[i][j] != 0) hasLine = true;
                }
            }
            if(hasLine == false) break;
            for(int i=N-1;i>0;i--) {
                for(int j=0;j<M;j++) {
                    Map[i][j] = Map[i - 1][j];
                }
            }
            for(int j=0;j<M;j++) Map[0][j] = 0;
        }
    }
    int getBlocks() {
        int ret = 0;
        for(int i=6;i<10;i++) {
            for(int j=0;j<M;j++) {
                if(Map[i][j] == 1) ret++;
            }
        }
        return ret;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    int answer = 0;
    Board Green, Blue;
    for(int i=0;i<N;i++) {
        int t, x, y; cin >> t >> x >> y;
        if(t == 1) {
            Green.put(t, x, y);
            Blue.put(t, y, x);
        }
        else {
            Green.put(t, x, y);
            Blue.put(5-t, y, x);
        }

        answer += Green.checkLine();
        answer += Blue.checkLine();
        Green.eraseLine();
        Blue.eraseLine();
    }
    cout << answer << '\n';
    cout << Green.getBlocks() + Blue.getBlocks() << '\n';

    return 0;
}
