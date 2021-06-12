// Authored by : ropeiny
// Co-authored by : -
// Link : http://boj.kr/60d75fb14ea446dfa3de373804b2a1c6
#include<bits/stdc++.h>

using namespace std;

int N, M;
int maps[501][501];
int dp[501][501];

int dfs(int n, int m, int val) {

    if (n == N && m == M) return 1;
    if (dp[n][m] != -1) return dp[n][m];

    dp[n][m] = 0;

    if (n + 1 <= N && val > maps[n + 1][m]) dp[n][m] += dfs(n + 1, m, maps[n + 1][m]);
    if (n - 1 >= 1 && val > maps[n - 1][m]) dp[n][m] += dfs(n - 1, m, maps[n - 1][m]);
    if (m + 1 <= M && val > maps[n][m + 1]) dp[n][m] += dfs(n, m + 1, maps[n][m + 1]);
    if (m - 1 >= 1 && val > maps[n][m - 1]) dp[n][m] += dfs(n, m - 1, maps[n][m - 1]);

    return dp[n][m];
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> maps[i][j];
        }
    }

    memset(dp, -1, sizeof(dp));

    cout << dfs(1, 1, maps[1][1]) << '\n';

    return 0;
}
