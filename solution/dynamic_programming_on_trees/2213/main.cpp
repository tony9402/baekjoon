// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/915dd2a773bc42b0ac94966f6ef852e6
#include<bits/stdc++.h>

using namespace std;

const int MAXN = 10005;
vector<int> graph[MAXN], answer;
int cost[MAXN], DP[MAXN][2];
bool used[MAXN];

void dfs(int cur, int prv) {
    for(auto &nxt: graph[cur]) {
        if(nxt == prv) continue;
        dfs(nxt, cur);
        DP[cur][0] += max(DP[nxt][0], DP[nxt][1]);
        DP[cur][1] += DP[nxt][0];
    }
    DP[cur][1] += cost[cur];
    used[cur] = DP[cur][1] > DP[cur][0];
}

void trace(int cur, int prv) {
    if(used[cur]) answer.push_back(cur);
    for(auto &nxt: graph[cur]) {
        if(nxt == prv)continue;
        if(used[cur]) used[nxt] = 0;
        trace(nxt, cur);
    }
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
    trace(1, 1);
    cout << max(DP[1][0], DP[1][1]) << '\n';
    sort(answer.begin(), answer.end());
    for(auto &i: answer)cout << i << ' ' ;

    return 0;
}
