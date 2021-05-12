// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/d46daeae8c194cb080f41f07b383b113
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

unordered_map<ll, ll> mp;
ll prefix[200002];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll N, K; cin >> N >> K;
    ll answer = 0;
    for(int i=1;i<=N;i++) {
        cin >> prefix[i];
        prefix[i] += prefix[i - 1];

        if(prefix[i] == K) answer ++;

        if(mp.count(prefix[i] - K)) answer += mp[prefix[i] - K];
        mp[prefix[i]] ++;
    }
    cout << answer;

    return 0;
}
