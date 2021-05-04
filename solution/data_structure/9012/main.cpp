#include<bits/stdc++.h>

using namespace std;

string solve(string str) {
    stack<int> st; //스택을 안써도 되긴 함
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
