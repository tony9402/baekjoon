// author    : seastar105
// Co-author : -
// Link      : http://boj.kr/08105c2def084cadbdf8ee2e4549d525
#include<bits/stdc++.h>
using namespace std;
const int MAX = 100000;
int dist[100005];
int N, K;

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> N >> K;
    memset(dist, -1, sizeof(dist));
    queue<int> q;
    dist[N] = 0;
    q.push(N);
    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        int pw = cur * 2;
        while(0 <= pw && pw <= MAX) {
            if(dist[pw] == -1) {
                dist[pw] = dist[cur];
                q.push(pw);
            }
            else break;
            pw *= 2;
        }
        if(cur > 0 && dist[cur-1] == -1) {
            dist[cur-1] = dist[cur] + 1;
            q.push(cur-1);
        }
        if(cur < MAX && dist[cur+1] == -1) {
            dist[cur+1] = dist[cur] + 1;
            q.push(cur+1);
        }
    }
    cout << dist[K] << '\n';
    return 0;
}
