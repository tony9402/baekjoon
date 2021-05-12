// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/619d768333f74fce8dd3e0cdd129a675
#include<bits/stdc++.h>

using namespace std;

bool arr[6666][6666];

void solve(int y, int x, int size) {
    if(size == 3) {
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                if(i == 1 && j == 1)continue;
                arr[y + i][x + j] = true;
            }
        }
        return;
    }
    size /= 3;
    solve(y + 0 * size, x + 0 * size, size);
    solve(y + 0 * size, x + 1 * size, size);
    solve(y + 0 * size, x + 2 * size, size);
    solve(y + 1 * size, x + 0 * size, size);

    solve(y + 1 * size, x + 2 * size, size);
    solve(y + 2 * size, x + 0 * size, size);
    solve(y + 2 * size, x + 1 * size, size);
    solve(y + 2 * size, x + 2 * size, size);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    solve(0, 0, N);
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(arr[i][j]) cout << "*";
            else cout << " ";
        }
        cout << '\n';
    }

    return 0;
}
