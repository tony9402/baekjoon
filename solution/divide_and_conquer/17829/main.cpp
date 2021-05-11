// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/aa7f1c4041eb4941a1366dd8229e70a4
#include<bits/stdc++.h>

using namespace std;

constexpr int MAXN = 1025;
int arr[MAXN][MAXN], tmp[MAXN][MAXN];

void f(int y, int x, int s) {
    if(s == 2) {
        int value[4] = { 0 };
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                value[i * 2 + j] = arr[y + i][x + j];
            }
        }
        sort(value, value + 4);
        tmp[y / 2][x / 2] = value[2];
        return;
    }

    s /= 2;
    f(y    , x    , s);
    f(y + s, x    , s);
    f(y    , x + s, s);
    f(y + s, x + s, s);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> arr[i][j];
        }
    }

    while(N != 1) {
        f(0, 0, N);
        N /= 2;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                arr[i][j] = tmp[i][j];
            }
        }
    }
    cout << arr[0][0];

    return 0;
}
