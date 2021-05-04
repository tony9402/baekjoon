#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K; cin >> N >> K;
    queue<int> Q;
    for(int i=1;i<=N;i++) Q.push(i);
    cout << "<";
    while(true) {
        for(int i=1;i<K;i++) {
            Q.push(Q.front());
            Q.pop();
        }
        cout << Q.front(); Q.pop();
        if(!Q.empty()) cout << ", ";
        else break;
    }
    cout << ">";

    return 0;
}
