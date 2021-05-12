// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9916726bfd8e4ded9c7e4d6295073c1f
#include<bits/stdc++.h>

using namespace std;

const int dy[] = { 1, 0 };
const int dx[] = { 0, 1 };
int DP[1002][1002][4], V[1002][1002], N;

int go(int y, int x, int milk) {
    int &ret = DP[y][x][milk + 1];
    if(ret != -1) return ret;
    ret = 0;
    for(int dir = 0; dir < 2; dir++) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];
        if(0 > ny || ny >= N || 0 > nx || nx >= N) continue;
        if(V[ny][nx] == (milk + 1) % 3) ret = max(ret, go(ny, nx, (milk + 1) % 3) + 1);
        ret = max(ret, go(ny, nx, milk));
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            cin >> V[i][j];
        }
    }
    memset(DP, 0xff, sizeof(int) * 1002 * 1002 * 4);
    if(V[0][0] == 0) cout << go(0, 0, 0) + 1;
    else cout << go(0, 0, -1);

    return 0;
}
