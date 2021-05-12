// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/41809c7260ee45f0919c4bd54da18518
#include<bits/stdc++.h>

using namespace std;

const string INIT = "wgorby";
const string DB = "ULBFRD";
string cube = "";
const int turn[][12] = {
    {17, 14, 11, 24, 25, 26, 36, 39, 42, 29, 28, 27}, // U
    {18, 21, 24,  0,  3,  6, 27, 30, 33, 53, 50, 47}, // L
    { 2,  1,  0, 11, 10,  9, 47, 46, 45, 38, 37, 36}, // B
    {15, 16, 17,  6,  7,  8, 42, 43, 44, 51, 52, 53}, // F
    {35, 32, 29,  8,  5,  2, 26, 23, 20, 45, 48, 51}, // R
    {44, 41, 38, 20, 19, 18,  9, 12, 15, 33, 34, 35}  // D
};

void init() {
    cube = "";
    for(int i=0;i<(int)INIT.size();i++) cube += string(9, INIT[i]);
}

int getFace(char x) {
    for(int i=0;i<(int)DB.size();i++) if(DB[i] == x) return i;
    return -1;
}

void execute(const string &cmd) {
    int faceNumber   = getFace(cmd[0]);
    const int *move  = turn[faceNumber];
    bool rev         = cmd[1] == '-';
    int executeCount = rev ? 3 : 1;

    for(int k=0;k<executeCount;k++){
        int base = faceNumber * 9;
        char tmp[3][3] = { };
        for(int i=0;i<3;i++)for(int j=0;j<3;j++)tmp[i][j] = cube[base + i * 3 + j];
        for(int i=0;i<3;i++)for(int j=0;j<3;j++)cube[base + j * 3 + 2 - i] = tmp[i][j];
        for(int i=0;i<3;i++){
            char nxt = cube[move[3 * 3 + i]];
            for(int j=0;j<4;j++) swap(cube[move[3 * j + i]], nxt);
        }
    }
}

void print(int faceNumber) {
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout << cube[faceNumber * 9 + i * 3 + j];
        }
        cout << '\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        init();
        int Q; cin >> Q;
        while(Q--) {
            string s; cin >> s;
            execute(s);
        }
        print(0);
    }

    return 0;
}
