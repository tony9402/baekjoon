//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/1744c1e07a70449ba28fd54faab4b25b
#include <bits/stdc++.h>

using namespace std;

char chess[10][10];
bool visited[10][10];
int wall_count = 0; 
int dx[] = {1, 0, -1, 0, 1, -1, 1, -1, 0};
int dy[] = {0, 1, 0, -1, -1, 1, 1, -1, 0};

void moveWall() {
    for(int i = 8;i > 0;i--) {
        for(int j = 1;j <= 8;j++) {
            if(chess[i][j] != '#') continue;

            int nextwall = i + 1;
            if(nextwall <= 8) {
                chess[nextwall][j] = '#';
                chess[i][j] = '.';
            }
            else {
                chess[i][j] = '.';
                wall_count--;
            }
        }
    }
}

bool bfs() {
    queue<pair<int, int>> q;
    q.push(make_pair(8, 1));

    // 현재위치에서 다음 위치로 갈 수 있는 곳을 큐에 집어넣고
    // 다음 while roop에서 전에 넣었던 위치를 반드시 다 방문한 후
    // 벽을 움직여야한다. 따라서 check이 queue의 크기를 저장하고
    // check만큼 다 방문한 후에 moveWall()을 실행한다.
    // 그래야 갈 수 있는 모든 경우의 수를 확인할 수 있다.
    while(!q.empty()) {
        int check = q.size();

        for(int i = 0;i < check;i++) {
            pair cur = q.front();
            q.pop();

            if(chess[cur.first][cur.second] == '#') continue;

            if((cur.first == 1 && cur.second == 8) || wall_count == 0) return true;

            // 8방향 + 제자리 총 9방향을 검사합니다.
            for(int j = 0;j < 9;j++) {
                int nexty = cur.first + dy[j];
                int nextx = cur.second + dx[j];

                if(nextx <= 0 || nexty <= 0 || nextx > 8 || nexty > 8) continue;
                if(visited[nexty][nextx] == true || chess[nexty][nextx] == '#') continue;

                visited[nexty][nextx] = true;
                q.push(make_pair(nexty, nextx));
            }
        }

        for(int i = 0;i < 10;i++)
            memset(visited[i], false, 10 * sizeof(bool));

        if(wall_count > 0) moveWall();
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);

    // 입력과 동시에 벽 개수를 카운트 합니다.
    for(int i = 1;i <= 8;i++) {
        string str;
        cin >> str;
        for(int j = 1;j <= 8;j++) {
            chess[i][j] = str[j - 1];
            if(chess[i][j] == '#') wall_count++;
        }
    }

    if(bfs() == true) cout << "1";
    else cout << "0";

    return 0;
} 
