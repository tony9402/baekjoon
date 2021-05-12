// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/553d0936c1674183a249a58070467343
#include<bits/stdc++.h>

using namespace std;

string solve(string str) {
    stack<int> st; 
    for(int i=0;i<(int)str.size();i++){
        if(str[i] == '(') st.push('(');
        else {
            if(st.empty()) return "NO";
            st.pop();
        }
    }

    if(st.empty()) return "YES";
    return "NO";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        string s; cin >> s;
        cout << solve(s) << '\n';
    }

    return 0;
}
