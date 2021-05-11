// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/3866a743ca954b6fa27922ed08da2b5e
#include<bits/stdc++.h>

using namespace std;

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++){
        int x; cin >> x;
        if(x == 0) {
            if(pq.empty()) cout << 0 << '\n';
            else {
                cout << pq.top().second << '\n';
                pq.pop();
            }
        }
        else pq.emplace(abs(x), x);
    }

    return 0;
}
