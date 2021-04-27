#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
ll prefix[4004][4004], V[2002][2002], ans[2002][2002];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;

    int dx = M / 2;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=N;j++) {
            cin >> V[i][j];
            prefix[i + M - 1][j + M - 1] = prefix[i + M - 2][j + M - 1] + prefix[i + M - 1][j + M - 2] - prefix[i + M - 2][j + M - 2];
            ans[i + dx][j + dx] = -(V[i][j] + prefix[i + M - 1][j + M - 1] - prefix[i - 1][j + M - 1] - prefix[i + M - 1][j - 1] + prefix[i - 1][j - 1]);
            prefix[i + M - 1][j + M - 1] += ans[i + dx][j + dx];
        }
    }
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=N;j++) {
            cout << ans[i][j] << " ";
        }
        cout << '\n';
    }

    return 0;
}
