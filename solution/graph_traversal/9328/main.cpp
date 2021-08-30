// Authored by : xhdxhl
// Co-authored by : -
// Link : http://boj.kr/6993dc4aebe24e399f02ac7fd5b2c0f8

#include <bits/stdc++.h>
using namespace std;

struct Coords{ int r, c; };

int dr[] = {0,0,-1,1};
int dc[] = {1,-1,0,0};
int n, m, testCase, countDoc, ck[101][101];
char building[101][101];
map <char, int> keys;
vector <Coords> entry;

//테두리에 있는 출입구 모두 찾아 entry에 push
void pushEntries(){
    for(int col = 0; col < m; col++){
        if(building[0][col] != '*')
            entry.push_back({0,col});
    }
    for(int row = 1; row < n; row++){
        if(building[row][m-1] != '*')
            entry.push_back({row,m-1});
    }

    for(int col = m-2; col >= 0; col--){
        if(building[n-1][col] != '*' )
            entry.push_back({n-1,col});
    }

    for(int row = 1; row < n - 1; row++){
        if(building[row][0] != '*')
            entry.push_back({row,0});
    }
}

int bfs(){
    int isNeedUpdate = 0;
    memset(ck,0,sizeof(ck));
    queue <Coords> q;

    for(auto e : entry) {
        if('A' <= building[e.r][e.c] && building[e.r][e.c] <= 'Z'){
            if(keys.count(building[e.r][e.c] -'A' + 'a')) building[e.r][e.c] = '.';
            else continue;
        }
        if('a' <= building[e.r][e.c] && building[e.r][e.c] <= 'z'){
            keys[building[e.r][e.c]] = 1;
        }
        q.push({e.r, e.c});
        ck[e.r][e.c] = 1;
        if(building[e.r][e.c] == '$') building[e.r][e.c] = '.', countDoc++;
    }
    
    while(!q.empty()){
        int r = q.front().r;
        int c = q.front().c;
        q.pop();
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(0 > nr || nr >= n || 0 > nc || nc >= m) continue;
            if(building[nr][nc] == '*' || ck[nr][nc]) continue;
            if('A' <= building[nr][nc] && building[nr][nc] <= 'Z'){
                char key = building[nr][nc] - 'A' + 'a';
                if(keys.count(key) == 0) continue;
                isNeedUpdate = 1;
            }

            if(building[nr][nc] == '$') countDoc++;
            if('a' <= building[nr][nc] && building[nr][nc] <= 'z') {
                keys[building[nr][nc]] = 1;
                isNeedUpdate = 1;
            }

            building[nr][nc] = '.';
            ck[nr][nc] = 1;
            q.push({nr,nc});
        }
    }
    return isNeedUpdate;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> testCase;
    while(testCase--){
        keys.clear();
        entry.clear();
        countDoc = 0;
        cin >> n >> m;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin >> building[i][j];
            }
        }

        string keyInPossession;
        cin >> keyInPossession;

        for(auto k : keyInPossession) keys[k] = 1;
        
        pushEntries();
        while(bfs());
        cout << countDoc << '\n';
    }
}

// 설명 : https://github.com/tony9402/baekjoon/pull/255#issue-722190601
