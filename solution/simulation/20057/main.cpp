// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/0b0d9c188523450dac94997ea85f81f5
#include<bits/stdc++.h>

using namespace std;

int Map[555][555], N;
const int dy [] = {0,1,0,-1};
const int dx [] = {-1,0,1,0};
bool inrange(int y, int x) { return 0 <= y && y < N && 0 <= x && x < N; }
int arr[5][5] = { 
    {0, 0, 2, 0, 0},
    {0,10, 7, 1, 0},
    {5, 0, 0, 0, 0},
    {0,10, 7, 1, 0},
    {0, 0, 2, 0, 0}
};

void Turn() {
    int tmp[5][5] = { };
    for(int i=0;i<5;i++) for(int j=0;j<5;j++) tmp[i][j] = arr[i][j];
    for(int i=0;i<5;i++) for(int j=0;j<5;j++) arr[4-j][i] = tmp[i][j];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for(int i=0;i<N;i++) 
        for(int j=0;j<N;j++)
            cin >> Map[i][j];

    int y = N / 2, x = N / 2;
    int answer = 0, cur = 2, dir = 0;

    bool flag = false;
    while(true) {
        int cnt = cur / 2;
        if(flag) cnt --;
        for(int i=0;i<cnt;i++) {
            y += dy[dir];
            x += dx[dir];
            int value = Map[y][x];
            for(int l=-2;l<3;l++){
                for(int m=-2;m<3;m++){
                    if(arr[l + 2][m + 2] == 0) continue;
                    int cury = y + l, curx = x + m;
                    int curvalue = value * arr[l + 2][m + 2] / 100;
                    Map[y][x] -= curvalue;
                    if(!inrange(cury, curx)) answer += curvalue;
                    else Map[cury][curx] += curvalue;
                }
            }
            int ny = y + dy[dir];
            int nx = x + dx[dir];
            if(inrange(ny, nx)) Map[ny][nx] += Map[y][x];
            else answer += Map[y][x];
            Map[y][x] = 0;
        }
        if(flag) break;
        if(++cur / 2 == N) flag = true;
        dir = (dir + 1) % 4;
        Turn();
    }

    cout << answer;
    return 0;
}
