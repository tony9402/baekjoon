#include<bits/stdc++.h>

using namespace std;

priority_queue<int, vector<int>, greater<int>> pq;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            int x;cin >> x;
            pq.push(x);
            if((int)pq.size() > N) pq.pop();
        }
    }
    cout << pq.top();

    return 0;
}
