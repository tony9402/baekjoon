// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/1df192eb8ca749ec8a568e9189e4ef5d
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        string s; cin >> s;
        bool flag = true;
        int idx = 0, N = (int)s.size();
        if(idx < N && 'B' <= s[idx] && s[idx] <= 'F') idx++;
        for(char cur : {'A', 'F', 'C'}) {
            int cnt = 0;
            while(idx < N && s[idx] == cur) idx++, cnt++;
            if(cnt == 0) flag = false;
        }
        if(idx < N && 'A' <= s[idx] && s[idx] <= 'F') idx++;
        if(idx < N) flag = false;
        if(flag) cout << "Infected!\n";
        else cout << "Good\n";
    }

    return 0;
}
