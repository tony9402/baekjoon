#include<bits/stdc++.h>

using namespace std;

unordered_set<string> st;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=0;i<N;i++) {
        string s; cin >> s;
        st.insert(s);
    }
    
    int answer = 0;
    for(int i=0;i<M;i++){
        string s; cin >> s;
        // st.count(s) != 0 으로 체크 해도 됨.
        if(st.find(s) != st.end()) answer ++;
    }
    cout << answer;

    return 0;
}
