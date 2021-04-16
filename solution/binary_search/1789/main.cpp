#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll S;
bool chk(ll n){ return n*(n+1)/2 > S; }

int main(){
    cin >> S;
    ll l = 1, r = 93000; // sqrt(4294967295 * 2)
    while(l <= r){
        ll mid = (l + r) / 2;
        if(chk(mid))r = mid - 1;
        else l = mid + 1;
    }
    cout << r;
}
