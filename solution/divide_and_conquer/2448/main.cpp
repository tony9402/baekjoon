// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ef87750a456447a59d9ba95d57c1f10b
#include<bits/stdc++.h>

using namespace std;

char stars[3500][6500];
char DB[3][6] = {
    "  *  ",
    " * * ",
    "*****"
};

void solve(int y, int x, int s) {
    if(s == 1) {
        for(int i=0;i<3;i++){
            for(int j=0;j<5;j++){
                stars[y + i][x + j] = DB[i][j];
            }
        }
        return;
    }
    s /= 2;
    solve(y, x + 3 * s, s);
    solve(y + 3 * s, x, s);
    solve(y + 3 * s, x + 6 * s, s);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    solve(0, 0, n / 3);
    for(int i=0;i<n;i++){
        for(int j=0;j<2*n-1;j++){
            if(stars[i][j] == '*') cout << '*';
            else cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
