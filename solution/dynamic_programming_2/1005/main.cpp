// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9577f93393b64444a01592dfb1458d97
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        int N, M, W; cin >> N >> M;
        vector<vector<int>> graph(N);
        vector<int> V(N), DP(N), indegree(N);
        for(int i=0;i<N;i++) cin >> V[i];
        for(int i=0;i<M;i++) {
            int a, b; cin >> a >> b;
            graph[--a].emplace_back(--b);
            indegree[b]++;
        }
        cin >> W;

        queue<int> Q;
        for(int i=0;i<N;i++){
            if(!indegree[i]) {
                Q.push(i);
                DP[i] = V[i];
            }
        } 

        while(!Q.empty()) {
            int cur = Q.front(); Q.pop();
            for(auto &nxt: graph[cur]) {
                if(--indegree[nxt] == 0) Q.push(nxt);
                DP[nxt] = max(DP[nxt], DP[cur] + V[nxt]);
            }
        }

        cout << DP[--W] << '\n';
    }

    return 0;
}
