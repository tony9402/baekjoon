// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a9ecf254aa654c0f878079eee6e2a275
#include<bits/stdc++.h>

using namespace std;

constexpr int dy[] = {-1,0,0,1};
constexpr int dx[] = {0,-1,1,0};

int Map[22][22], n;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    int sy, sx;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin >> Map[i][j];
            if(Map[i][j] == 9)sy = i, sx = j;
        }
    }

    bool done = true;
    int ate = 2, sharkSize = 2;
    int answer = 0;
    while(done){
        bool visited[22][22] = { };
        int ny = -1, nx = -1, times = -1;
        Map[sy][sx] = 0;
        
        queue<pair<int, int>> q;
        q.push(pair<int, int>(sy, sx));
        visited[sy][sx] = true;

        while(!q.empty()){
            int qsize = q.size();
            ++times;
            while(qsize--){
                auto [y, x] = q.front(); q.pop();
                if(Map[y][x] && Map[y][x] < sharkSize){
                    if(!~ny)ny = y, nx = x;
                    else {
                        if(y < ny)ny = y, nx = x;
                        else if(y == ny && x < nx)nx = x;
                    }
                }
                
                for(int k=0;k<4;k++){
                    int qy = y + dy[k];
                    int qx = x + dx[k];
                    if(0 > qy || qy >= n || 0 > qx || qx >= n)continue;
                    if(visited[qy][qx])continue;
                    visited[qy][qx] = true;
                    if(Map[qy][qx] > sharkSize)continue;
                    q.push(pair<int, int>(qy, qx));
                } 
            }
            if(~ny){
                if(--ate == 0)ate = ++sharkSize;
                break;
            }
        }

        sy = ny, sx = nx;
        if(!~ny)done = false;
        else answer += times;
    }

    cout << answer;

    return 0;
}
