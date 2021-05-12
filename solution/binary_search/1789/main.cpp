// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/b757695822a7451ca902c666e024bb5f
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll S;
bool chk(ll n){ return n*(n+1)/2 > S; }

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> S;
    ll l = 1, r = 93000; // sqrt(4294967295 * 2)
    while(l <= r){
        ll mid = (l + r) / 2;
        if(chk(mid))r = mid - 1;
        else l = mid + 1;
    }
    cout << r;
}
