// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/5bf67529d3a7434d9c53943021aff0ff
#include<bits/stdc++.h>

using namespace std;

unordered_set<int> st;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K; cin >> N >> K;
    queue<pair<long long, long long>> Q;
    vector<long long> V;
    for(int i=0;i<N;i++) {
        long long x;cin >> x;
        V.push_back(x);
        st.insert(x);
    }
    for(auto x: V){
        if(st.count(x - 1) == 0) {
            Q.emplace(x, x - 1);
            st.insert(x - 1);
        }
        if(st.count(x + 1) == 0) {
            Q.emplace(x, x + 1);
            st.insert(x + 1);
        }
    }
    long long answer = 0;
    while(K--) {
        auto [city, cur] = Q.front(); Q.pop();
        answer += abs(city - cur);
        if(st.count(cur - 1) == 0) {
            st.insert(cur - 1);
            Q.emplace(city, cur - 1);
        }
        if(st.count(cur + 1) == 0) {
            st.insert(cur + 1);
            Q.emplace(city, cur + 1);
        }
    }
    cout << answer;

    return 0;
}
