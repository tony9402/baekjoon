// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/72c8c91b832f4245a081dca0285edd18
#include<bits/stdc++.h>

using namespace std;

const string DB[8] = { "0", "0", "1", "7", "4", "2", "0", "8" };
string minstr[105] = { "0", "0", "1", "7", "4", "2", "6", "8", "10" };
string maxstr[105];

string getMax(int cnt) {
    string ans;
    while(cnt) {
        if(cnt & 1) {
            ans += '7';
            cnt -= 3;
        }
        else {
            ans += '1';
            cnt -= 2;
        }
    }
    return ans;
}

string getMin(const string &a, const string &b) {
    if(a.size() > b.size()) return b;
    if(a.size() < b.size()) return a;
    for(int i=0;i<(int)a.size();i++){
        if(a[i] < b[i]) return a;
        if(a[i] > b[i]) return b;
    }
    return a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    for(int i=2;i<=100;i++)maxstr[i] = getMax(i);
    for(int i=9;i<=100;i++){
        minstr[i] = minstr[i - 2] + DB[2];
        for(int j=3;j<=7;j++) minstr[i] = getMin(minstr[i], minstr[i - j] + DB[j]);
    }
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        cout << minstr[n] << " " << maxstr[n] << '\n';
    }

    return 0;
}
