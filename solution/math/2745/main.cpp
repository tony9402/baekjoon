// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/6f8324f145664e3890bd12301389737d
#include<bits/stdc++.h>

using namespace std;

int getValue(char x) {
    if(x <= '9') return x - '0';
    return x - 'A' + 10;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s; cin >> s;
    int base; cin >> base;
    
    int answer = 0;
    for(int i=0;i<(int)s.size();i++) {
        answer = answer * base + getValue(s[i]);
    }
    cout << answer;

    return 0;
}
