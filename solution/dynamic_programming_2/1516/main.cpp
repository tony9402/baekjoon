// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/10dc239cb8764cbf88f4745de6cd2fa8
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N; cin >> N;
    vector<vector<int>> graph(N);
    vector<int> V(N), DP(N), indegree(N);
    for(int i=0;i<N;i++) {
        cin >> V[i];
        while(true) {
            int x; cin >> x;
            if(x == -1) break;
            graph[--x].push_back(i);
            indegree[i] ++;
        }
    }

    queue<int> Q;
    for(int i=0;i<N;i++) {
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
    for(int i=0;i<N;i++) cout << DP[i] << '\n';

    return 0;
}
