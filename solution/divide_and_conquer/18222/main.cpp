// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9573c1f4e8924a1b8f19ce128d132a68
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll N; cin >> N;
    ll cnt = 0;
    while(N){
        ll cur = 1;
        while(cur * 2 < N) cur <<= 1;
        N -= cur;
        cnt ++;
    }
    ll ans = ~cnt & 1;
    cout << ans;

    return 0;
}

