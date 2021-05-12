// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/4e60b2336bfa4e3192b9aef4eb5a3f6b
#include<bits/stdc++.h>

using namespace std;

const int dy[] = {-1,1,0,0};
const int dx[] = {0,0,-1,1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int K, Q; cin >> K >> Q;
    int N = 1 << K;
    vector<vector<int>> Map(N, vector<int>(N));
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> Map[i][j];
        }
    }

    while(Q--) {
        int L; cin >> L;
        int M = 1 << L;
        vector<vector<int>> tmp = Map;
        for(int i=0;i<N;i+=M){
            for(int j=0;j<N;j+=M){
                for(int m=0;m<M;m++){
                    for(int n=0;n<M;n++){
                        Map[i+n][j+M-1-m] = tmp[i+m][j+n];
                    }
                }
            }
        }
        tmp = Map;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(Map[i][j] == 0)continue;
                int cnt = 0;
                for(int k=0;k<4;k++) {
                    int qy = i + dy[k];
                    int qx = j + dx[k];
                    if(0 > qy || qy >= N || 0 > qx || qx >= N) continue;
                    if(Map[qy][qx] != 0) cnt ++;
                }
                if(cnt < 3) tmp[i][j] --;
            }
        }
        Map = tmp;
    }

    int total = 0;
    int mx    = 0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(Map[i][j] == 0)continue;
            total += Map[i][j];
            int cnt = 0;
            Map[i][j] = 0;
            queue<pair<int, int>> q;
            q.emplace(i, j);
            while(!q.empty()) {
                auto [y, x] = q.front(); q.pop();
                cnt++;
                for(int k=0;k<4;k++){
                    int qy = y + dy[k];
                    int qx = x + dx[k];
                    if(0 > qy || qy >= N || 0 > qx || qx >= N) continue;
                    if(Map[qy][qx] == 0)continue;
                    q.emplace(qy, qx);
                    total += Map[qy][qx];
                    Map[qy][qx] = 0;
                }
            }
            mx = max(mx, cnt);
        }
    }
    
    cout << total << '\n';
    cout << mx;

    return 0;
}
