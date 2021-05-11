// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/2bf5637604cb4c8589f9fbc18a16bca5
#include<bits/stdc++.h>

using namespace std;

int arr[150][150], answer[2];

void solve(int y, int x, int size) {
    bool flag = true;
    for(int i=0;i<size;i++) {
        for(int j=0;j<size;j++) {
            if(arr[y][x] != arr[y + i][x + j]) flag = false;
        }
    }

    if(flag) answer[arr[y][x]] ++;
    else {
        size /= 2;
        solve(y       , x       , size);
        solve(y + size, x       , size);
        solve(y       , x + size, size);
        solve(y + size, x + size, size);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            cin >> arr[i][j];
        }
    }

    solve(0, 0, N);
    cout << answer[0] << '\n' << answer[1];

    return 0;
}
