//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/9d2150583b8f404997ceb816aca057ac

#include <bits/stdc++.h>

using namespace std;

int castle[110][110], dist[110][110];
int N, M, T;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
bool visited[110][110];
pair<int, int> sword;

void bfs() {
    queue<pair<int, int>> q;
    q.push(make_pair(1, 1));
    visited[1][1] = true;

    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        for(int i = 0;i < 4;i++) {
            int nextx = cur.first + dx[i];
            int nexty = cur.second + dy[i];

            if(nextx <= 0 || nexty <= 0 || nextx > N || nexty > M) continue;
            if(visited[nextx][nexty] == true || castle[nextx][nexty] == 1) continue;

            q.push(make_pair(nextx, nexty));
            visited[nextx][nexty] = true;
            dist[nextx][nexty] = dist[cur.first][cur.second] + 1;
        }
    }
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);

    cin >> N >> M >> T;

    for(int i = 1;i <= N;i++) {
        for(int j = 1;j <= M;j++) {
            cin >> castle[i][j];
            if(castle[i][j] == 2)
                sword = make_pair(i, j);
        }
    }

    bfs();

    int use_sword = INT_MAX, not_use_sword = INT_MAX;

    // 검을 사용했을 때 걸리는 시간. 구하지 못하는 경우는 int형 최대값
    if(dist[sword.first][sword.second] != 0)
        use_sword = dist[sword.first][sword.second] + (N - sword.first) + (M - sword.second);

    //검을 사용하지 않고 걸리는 시간. 구하지 못하는 경우는 int형 최대값
    if(dist[N][M] != 0)
        not_use_sword = dist[N][M];

    //둘 중 작은 값을 T보다 작을때만 출력, 그 외는 Fail출력
    int answer = min(use_sword, not_use_sword);
    if(answer > T)
        cout << "Fail";
    else cout << answer;

    return 0;
} 
