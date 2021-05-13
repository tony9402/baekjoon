// Authored by : seastar105
// Co-authored by : -
// Link : http://boj.kr/f78a96ebfe9a42648e1e0bc67255916a
#include<bits/stdc++.h>
using namespace std;
int R, C, N;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
vector<string> a(201);
int fire_time[201][201];

bool valid(int x, int y) {
    return 0<=x && x<R && 0<=y && y<C;
}

void fire(int t) {
    for(int i=0;i<R;++i) {
        for(int j=0;j<C;++j) {
            if(fire_time[i][j] != t) continue;
            for(int k=0;k<4;++k) {
                int nx = i + dx[k];
                int ny = j + dy[k];
                if(!valid(nx, ny)) continue;
                if(fire_time[nx][ny] == t) continue;
                fire_time[nx][ny] = 0;
                a[nx][ny] = '.';
            }
            fire_time[i][j] = 0;
            a[i][j] = '.';
        }
    }
}

void set_all(int t) {
    for(int i=0;i<R;++i) {
        for(int j=0;j<C;++j) {
            if(a[i][j] == 'O') continue;
            a[i][j] = 'O';
            fire_time[i][j] = t+3;
        }
    }
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> R >> C >> N;
    for(int i=0;i<R;++i) {
        cin >> a[i];
        for(int j=0;j<C;++j) {
            if(a[i][j] == 'O') fire_time[i][j] = 3;
        }
    }
    for(int t=2;t<=N;++t) {
        if(t%2) fire(t);
        else set_all(t);
    }
    for(int i=0;i<R;++i) cout << a[i] << '\n';
    return 0;
}
