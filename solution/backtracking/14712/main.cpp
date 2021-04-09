#include<bits/stdc++.h>

using namespace std;

int N, M, Map[33][33]; // 1-index
int answer = 0;

bool check(int y, int x) {
    return Map[y-1][x] && Map[y][x-1] && Map[y-1][x-1];
}

void go(int y, int x) {
    if(y == N && x == M + 1) {
        answer ++;
        return;
    }
    for(int i=y;i<=N;i++) {
        for(int j=(i==y?x:1);j<=M;j++) {
            if(check(i, j)) continue;
            Map[i][j] = 1;
            go(i, j + 1);
            Map[i][j] = 0;
        }
    }
    answer ++;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> N >> M;
    go(1, 1);
    cout << answer;

    return 0;
}
