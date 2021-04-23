#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    stack<pair<int, int>> st;

    st.emplace(100000005, 0);
    for(int i=1;i<=N;i++) {
        int x; cin >> x;
        while(!st.empty() && st.top().first < x) st.pop();
        cout << st.top().second << ' ';
        st.emplace(x, i);
    }

    return 0;
}
