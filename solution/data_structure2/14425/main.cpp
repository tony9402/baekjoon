// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c8831b4a36e741ddb4ae083cc32902ef
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
        if(st.find(s) != st.end()) answer ++;
    }
    cout << answer;

    return 0;
}
