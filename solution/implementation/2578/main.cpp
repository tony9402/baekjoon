// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/6a874bc16cbc470eb3338e2ec945f180
#include<bits/stdc++.h>

using namespace std;

int board[5][5];
bool used[5][5];

bool bingo() {
    int line = 0;

    bool bingo = true;
    for(int i=0;i<5;i++){
        bingo = true;
        for(int j=0;j<5;j++){
            bingo &= used[i][j];
        }
        if(bingo) line ++;
        
        bingo = true;
        for(int j=0;j<5;j++){
            bingo &= used[j][i];
        }
        if(bingo) line ++;
    }

    bingo = true;
    for(int i=0;i<5;i++){
        bingo &= used[i][i];
    }
    if(bingo) line++;
    
    bingo = true;
    for(int i=0;i<5;i++){
        bingo &= used[4-i][i];
    }
    if(bingo) line++;

    return line >= 3;
}

void marking(int number){
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(board[i][j] == number) {
                used[i][j] = true;
                return;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cin >> board[i][j];
        }
    }

    for(int i=1;i<=25;i++){
        int x;cin >> x;
        marking(x);
        if(bingo()){
            cout << i;
            return 0;
        }
    }

    return 0;
}
