// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/1a1754c8c07c462e9d52af5ae146809c

#include<bits/stdc++.h>

using namespace std;

int N, M, Map[33][33]; // 1-index
int answer = 0;

bool check(int y, int x) {
    return Map[y-1][x] && Map[y][x-1] && Map[y-1][x-1];
}

void go(int usedCnt) {
    if(usedCnt == N * M) {
        answer ++;
        return ;
    }

    int y = usedCnt / M + 1;
    int x = usedCnt % M + 1;

    go(usedCnt + 1);
    if(!check(y, x)) {
        Map[y][x] = 1;
        go(usedCnt + 1);
        Map[y][x] = 0;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> N >> M;
    go(0);
    cout << answer;

    return 0;
}
