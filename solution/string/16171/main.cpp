// Authored by : rlawngus0910
// Co-authored by : tony9402
// Link : http://boj.kr/cddf85db4e694c0d8e9a20dddd32e653
#include <bits/stdc++.h>
using namespace std;
string input, s, k;
int main() {
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin >> input >> k;

    for (int i = 0; i < (int)input.length(); i++) {
        if('0' <= input[i] && input[i] <= '9') continue;
        s += input[i];
    }

    if (s.find(k) != string::npos) cout << "1";
    else cout << "0";
} 
