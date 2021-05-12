// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/07f3319d2d85433d8a9df15316fca395
#include<bits/stdc++.h>

using namespace std;

const string qwerty[3] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
const string OnlyLeft  = "qwertasdfgzxcv";
int X[33], Y[33];

bool isLeft(char x){ return OnlyLeft.find(x) != string::npos; }
int dist(char a, char b){return abs(Y[a-'a']-Y[b-'a']) + abs(X[a-'a']-X[b-'a']); }

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    for(int i=0;i<3;i++){
        for(int j=0;j<(int)qwerty[i].size();j++){
            Y[qwerty[i][j] - 'a'] = i;
            X[qwerty[i][j] - 'a'] = j;
        }
    }

    char L, R; cin >> L >> R;
    string word; cin >> word;

    int answer = 0;
    for(auto &w: word){
        if(isLeft(w)) {
            answer += dist(L, w) + 1;
            L = w;
        }
        else {
            answer += dist(R, w) + 1;
            R = w;
        }
    }
    cout << answer;

    return 0;
}

