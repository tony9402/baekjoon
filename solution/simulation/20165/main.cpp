// Authored by : klm03025
// Co-authored by : -
// Link : http://boj.kr/cf1f9691a2bc4d6795218d266c851386
#include <bits/stdc++.h>
using namespace std;

int dm_len[100][100];
bool dm_alive[100][100];

int N, M, R;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int score = 0;

void offense(int x, int y, char pos) {
    int idx;
    int dest = 0;
    if(pos == 'E') idx = 0;
    else if(pos == 'W') idx = 1;
    else if(pos == 'S') idx = 2;
    else idx = 3;

    if(!dm_alive[x][y]) return;
    score++;
    dm_alive[x][y] = 0;
    dest = dm_len[x][y];

    while(dest != 1) {
        dest--;
        x += dx[idx];
        y += dy[idx];

        if(x == N || x < 0 || y == M || y < 0) break;

        if(dm_alive[x][y]) {
            dest = max(dm_len[x][y], dest);
            score++;
        }
        dm_alive[x][y] = 0;

    }
}

void defense(int x, int y) {
    dm_alive[x][y] = 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> R;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> dm_len[i][j]; 
            dm_alive[i][j] = 1;           
        }
    }


    for(int i = 0; i < R; i++) {
        int x, y;
        char pos;

        cin >> x >> y >> pos;
        offense(x - 1, y - 1, pos);

        cin >> x >> y;
        defense(x - 1, y - 1);
    }

    cout << score << '\n';
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(dm_alive[i][j]) cout << 'S' << ' ';
            else cout << 'F' << ' ';
        }
        cout << '\n';
    }
}