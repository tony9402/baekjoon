// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/dc2b68715aff442db67228432e9510ed
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

bool chk(ll a, ll b) {
    if(b % a == 0) return a >= b / a;
    return a > b / a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll N; cin >> N;
    if(N == 0) {
        cout << 0;
        return 0;
    }
    ll L = 1, R = 1LL << 32;
    while(L <= R) {
        ll mid = L + (R - L) / 2;
        if(chk(mid, N)) R = mid - 1;
        else L = mid + 1;
    }
    cout << L;

    return 0;
}
