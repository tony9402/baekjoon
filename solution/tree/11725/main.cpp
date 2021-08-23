// Authored by : dart
// Co-authored by : -
// Link : http://boj.kr/d258432b92b14d9e87da9a05075a8052
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<int> adj[100005];
int parents[100005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(false);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int start, end;
        cin >> start >> end;
        adj[start].push_back(end);
        adj[end].push_back(start);
    }
    queue<int> Q;
    Q.push(1);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        for (int next:adj[cur]) {
            if (parents[next]) { continue; }
            parents[next] = cur;
            Q.push(next);
        }
    }
    for (int i = 2; i <= n; i++) {
        cout << parents[i] << "\n";
    }

    return 0;
}