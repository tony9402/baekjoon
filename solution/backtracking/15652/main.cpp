#include<bits/stdc++.h>

using namespace std;

int choose[10], N, M;

void dfs(int pre, int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << choose[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i=pre;i<=N;i++) {
        choose[cnt] = i;
        dfs(i, cnt + 1);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    dfs(1, 0);

    return 0;
}
