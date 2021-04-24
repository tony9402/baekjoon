#include<bits/stdc++.h>

using namespace std;
int arr[10][10], n, m, answer;
bool used[10][10];
bool ccheck[11][11];
pair<int, int> cases[4] = {{0,0}, {0,1}, {1,1}, {1,0}};

bool check(int y, int x, int c){
    int dy = cases[c].first, dx = cases[c].second;
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++){
            if(i == dy && j == dx)continue;
            if(i + y >= n || j + x >= m)return false;
            if(used[y+i][x+j])return false;
        }
    return true;
}

void change(int y, int x, int c){
    int dy = cases[c].first, dx = cases[c].second;
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++){
            if(i == dy && j == dx)continue;
            used[i+y][j+x] = !used[i+y][j+x];
        }
}

int cal(int y, int x, int c){
    int dy = cases[c].first, dx = cases[c].second;
    int oy = cases[(c+2)%4].first, ox = cases[(c+2)%4].second;
    int ret = 0;
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++){
            if(i == dy && j == dx) ret += arr[y+oy][x+ox];
            else ret += arr[y+i][x+j];
        }
    return ret;
}

int solve(int y, int x){
    int ret = 0;
    for(int i=y;i<n;i++){
        for(int j=(i == y ? x : 0);j<m;j++){
            for(int k=0;k<4;k++){
                if(!check(i,j,k))continue;
                change(i,j,k);
                int c = cal(i,j,k);
                c = c + solve(i, j);
                ret = max(ret, c);
                change(i,j,k);
            }
        }
    }
    answer = max(answer, ret);
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> n >> m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            cin >> arr[i][j];
        
    solve(0, 0);
    cout << answer;
}

