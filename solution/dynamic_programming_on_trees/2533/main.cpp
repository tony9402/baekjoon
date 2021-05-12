// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/24e0aea2f2c84d92a8c69035eb07916a
#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> graph, group;
vector<int> DP[2];

void dfs(int cur, int prv) {
    for(auto &nxt: graph[cur]) {
        if(nxt == prv)continue;
        group[cur].push_back(nxt);
        dfs(nxt, cur);
    }
}

int go(int cur, int toggle) {
    int &ret = DP[toggle][cur];
    if(ret != -1)return ret;
    ret = toggle;

    for(auto &nxt: group[cur]) {
        if(toggle) ret += min(go(nxt, 0), go(nxt, 1));
        else       ret += go(nxt, 1);
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    graph.resize(n + 1);
    group.resize(n + 1);
    DP[0] = DP[1] = vector<int>(n + 1, -1);

    for(int i=1;i<n;i++) {
        int a, b; cin >> a >> b;
        graph[a].emplace_back(b);
        graph[b].emplace_back(a);
    }

    dfs(1, 1);
    cout << min(go(1, 0), go(1, 1));

    return 0;
}
