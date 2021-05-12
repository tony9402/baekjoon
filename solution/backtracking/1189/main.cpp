// Authored by : jybin321
// Co-authored by : -
// Link : http://boj.kr/4e07968244514f549f599884c6fd819e

#include <bits/stdc++.h>
using namespace std;
int r, c, k, ans;
string _map[6];
bool visited[6][6];
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

void input() {
    cin >> r >> c >> k;
    for(int i = r - 1; i >= 0; i--) {
        string s; cin >> s;
        _map[i] = s;
    }
}

void func(int cnt, int y, int x) {
    if(cnt == k) {
        if(y == r - 1 && x == c - 1) ans += 1;
        return;
    }
    visited[y][x] = 1;
    for(int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if(nx < 0 || nx >= c || ny < 0 || ny >= r) continue;
        if(visited[ny][nx] || _map[ny][nx] == 'T') continue;
        func(cnt + 1, ny, nx);
        visited[ny][nx] = 0;
    }
}

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    input();
    func(1, 0, 0);
    cout << ans;
    return 0;
}