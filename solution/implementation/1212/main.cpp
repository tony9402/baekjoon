// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9aebf3cefd45466aa4c24dae72837024
#include<bits/stdc++.h>

using namespace std;

string convert(char s, bool fillzero=false){
    int n = s - 48;
    string ret = "";
    while(n){
        ret += (n % 2) + '0';
        n /= 2;
    }
    while(fillzero && (int)ret.size() < 3) ret += '0';
    reverse(ret.begin(), ret.end());
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s;cin >> s;
    if(s == "0") {
        cout << 0;
        return 0;
    }
    string ans="";
    for(int i=0;i<(int)s.size();i++){
        ans += convert(s[i], i != 0);
    }
    cout << ans;

    return 0;
}

