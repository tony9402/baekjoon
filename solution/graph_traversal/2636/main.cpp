// Authored by : bsoomin8734
// Co-authored by : tony9402
// Link : http://boj.kr/a7f85eb725a6477a919287e9e506db7b
#include <bits/stdc++.h>
using namespace std;

bool visited[101][101];
int Map[101][101];
int dir[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
int N, M;
queue<pair<int, int> > q;
int cnt = -1;
int result = 0;

void init(){
    while(!q.empty()) q.pop();
    q.emplace(0, 0);
    memset(visited, 0, sizeof(bool) * 101 * 101);
}

int BFS(){
    int cur_melt = 0;
    while(!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();

        for(int i = 0; i < 4; i++){
            int x = cur.first + dir[i][0];
            int y = cur.second + dir[i][1];
            if(0 > x || x >= N || 0 > y || y >= M) continue;
            if(visited[x][y]) continue;
            if(Map[x][y] == 0){
                visited[x][y] = true;
                q.emplace(x, y);
            } else if(Map[x][y] == 1){
                visited[x][y] = true;
                Map[x][y] = 0;
                cur_melt++;
            }
        }
    }
    return cur_melt;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            cin >> Map[i][j];

    while(1){
        init();
        cnt++;
        int ret = BFS();
        if(ret == 0) break;
        else result = ret;
    }

    cout << cnt << '\n' << result << '\n';

    return 0;
}
