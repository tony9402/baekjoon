// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c8fbfa4f718847b8a169037608c2e8be
#include<bits/stdc++.h>

using namespace std;

int uf[1005], N, K;
vector<vector<pair<int, int>>> graph;
vector<tuple<int, int, int>> V;

int find(int x) {
    if(uf[x] < 0)return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if(a == b)return false;
    uf[b] = a;
    return true;
}

pair<int, int> BFS(int s) {
    vector<int> visited(N);
    queue<pair<int, int>> Q;
    Q.emplace(s, 0);
    visited[s] = true;
    pair<int, int> ret = make_pair(0, 0); // [dist, node]
    while(!Q.empty()){
        auto [cur, dist] = Q.front(); Q.pop();
        ret = max(ret, make_pair(dist, cur));
        for(auto &[nxt, cost]: graph[cur]) {
            if(visited[nxt]) continue;
            visited[nxt] = true;
            Q.emplace(nxt, dist + cost);
        }
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    for(int i=0;i<1000;i++) uf[i] = -1;

    cin >> N >> K;
    graph.resize(N);
    for(int i=0;i<K;i++) {
        int a, b, c; cin >> a >> b >> c;
        V.emplace_back(c, a, b);
    }
    sort(V.begin(), V.end());

    int answer = 0;
    for(auto &[c, a, b]: V){
        if(merge(a, b)) {
            answer += c;
            graph[a].emplace_back(b, c);
            graph[b].emplace_back(a, c);
        }
    }

    cout << answer << '\n';
    cout << BFS(BFS(0).second).first;

    return 0;
}
