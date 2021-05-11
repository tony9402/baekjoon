// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/0a5ce31db1ff47cf8190b0275e74bef8
#include<bits/stdc++.h>

using namespace std;

int choose[10], N, M;

void dfs(int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << choose[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i=1;i<=N;i++) {
        choose[cnt] = i;
        dfs(cnt + 1);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    dfs(0);

    return 0;
}
