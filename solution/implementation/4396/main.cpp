// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a6ba32f17093473f9e0f5f3dee9f7ced
#include<bits/stdc++.h>

using namespace std;

vector<string> board, push;
const int dy[] = {0,0,-1,1,-1,-1,1,1};
const int dx[] = {-1,1,0,0,-1,1,-1,1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    board.resize(n); push.resize(n);
    for(int i=0;i<n;i++) cin >> board[i];
    for(int i=0;i<n;i++) cin >> push[i];

    bool pushed_mine = false;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(push[i][j] == '.')continue;
            if(board[i][j] == '*'){
                pushed_mine = true;
                continue;
            }
            int mine = 0;
            for(int k=0;k<8;k++){
                int qy = i + dy[k];
                int qx = j + dx[k];
                if(0 > qy || qy >= n || 0 > qx || qx >= n) continue;
                if(board[qy][qx] == '*') mine ++;
            }
            push[i][j] = (char)(mine + '0');
        }
    }
    
    if(pushed_mine){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j] == '*') push[i][j] = '*';
            }
        }
    }

    for(int i=0;i<n;i++) cout << push[i] << '\n';

    return 0;
}
