// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/627e3feffb1842298d6d7ce3093e807b
#include<bits/stdc++.h>

using namespace std;

const int MAXN = 10005;
vector<int> graph[MAXN];
int cost[MAXN], DP[MAXN][2];

void dfs(int cur, int prv) {
    for(auto &nxt: graph[cur]) {
        if(nxt == prv) continue;
        dfs(nxt, cur);
        DP[cur][0] += max(DP[nxt][0], DP[nxt][1]);
        DP[cur][1] += DP[nxt][0];
    }
    DP[cur][1] += cost[cur];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    for(int i=1;i<=n;i++) cin >> cost[i];
    for(int i=1;i< n;i++) {
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs(1, 1);
    cout << max(DP[1][0], DP[1][1]) << '\n';

    return 0;
}

