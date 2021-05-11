// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/cb5c5740111745b0b9f0fb6582da5bdd
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    queue<int> Q;
    for(int i=1;i<=N;i++) Q.push(i);
    while((int)Q.size() > 1) {
        Q.pop();
        Q.push(Q.front());
        Q.pop();
    }
    cout << Q.front();

    return 0;
}
