// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/fba04fa859d540fab6cad5266780f137
#include<bits/stdc++.h>

using namespace std;

int solve(int y, int x, int s) {
    if(s == 2) return 2 * y + x;
    s >>= 1;
    int ny = y / s, nx = x / s;
    int nxt = ny * 2 + nx;
    return s * s * nxt + solve(y - ny * s, x - nx * s, s);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, R, C; cin >> N >> R >> C;
    cout << solve(R, C, 1 << N);

    return 0;
}
