// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/bdcb1993d67a400c8293683e5c7dbf7d
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<ll> cost, dis, prefix;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N; cin >> N;
    cost.resize(N);
    dis.resize(N - 1);
    prefix.resize(N);
    for(int i=0;i<N-1;i++) cin >> dis[i];
    for(int i=0;i<N;i++) {
        prefix[i + 1] = prefix[i] + dis[i];
        cin >> cost[i];
    }
    int R = 0;
    ll answer = 0;
    for(int i=0;i<N-1;){
        while(R < N && cost[i] <= cost[R]) R++;
        if(R == N) --R;
        answer += cost[i] * (prefix[R] - prefix[i]);
        i = R;
    }
    cout << answer;

    return 0;
}

