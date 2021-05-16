// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/1bff0abd9f2646ceb07d7fdb4b5ace97
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s; cin >> s;
    stack<char> st;
    string answer = "";
    for(auto &ch: s) {
        if('A' <= ch && ch <= 'Z') answer += ch;
        else {
            if(ch == '(') st.push(ch);
            else if(ch == ')') {
                while(!st.empty() && st.top() != '(') {
                    answer += st.top();
                    st.pop();
                }
                st.pop();
            }
            else if(ch == '*' || ch == '/') {
                while(!st.empty() && (st.top() == '*' || st.top() == '/')) {
                    answer += st.top();
                    st.pop();
                }
                st.push(ch);
            }
            else if(ch == '+' || ch == '-') {
                while(!st.empty() && st.top() != '(') {
                    answer += st.top();
                    st.pop();
                }
                st.push(ch);
            }
        }
    }
    while(!st.empty()) {
        answer += st.top();
        st.pop();
    }
    cout << answer;

    return 0;
}

