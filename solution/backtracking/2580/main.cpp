// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/0ceb759a209343af89d8559da57a2bb2
#include<bits/stdc++.h>

using namespace std;

int Quiz[9][9], zeroCnt; 
bool y[9][10], x[9][10], xy[9][10];

void input() {
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin >> Quiz[i][j];
            if(Quiz[i][j] == 0)zeroCnt++;
            else {
                x[j][Quiz[i][j]] = true;
                y[i][Quiz[i][j]] = true;
                xy[i/3*3+j/3][Quiz[i][j]] = true;
            }
        }
    }
}

void output() {
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cout << Quiz[i][j] << " ";
        }
        cout << '\n';
    }
}

bool solve() {
    if(zeroCnt == 0) return true;

    // Find 0
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(Quiz[i][j] != 0) continue;
            for(int k=1;k<=9;k++){
                if(x[j][k] || y[i][k] || xy[i/3*3+j/3][k]) continue;
                x[j][k] = y[i][k] = xy[i/3*3+j/3][k] = true;
                Quiz[i][j] = k;
                zeroCnt--;
                if(solve()) return true;
                x[j][k] = y[i][k] = xy[i/3*3+j/3][k] = false;
                Quiz[i][j] = 0;
                zeroCnt++; 
            }
            return false;
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    input();
    solve();
    output(); 
}
