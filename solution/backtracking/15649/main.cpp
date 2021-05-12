// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/51963cf92cd741ea8bb67b164cc944f9
#include<bits/stdc++.h>

using namespace std;

int choose[10], N, M;
bool used[10];

void dfs(int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << choose[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i=1;i<=N;i++) {
        if(used[i]) continue;
        used[i] = true;
        choose[cnt] = i;
        dfs(cnt + 1);
        used[i] = false;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    dfs(0);

    return 0;
}
