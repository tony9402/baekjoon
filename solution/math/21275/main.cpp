// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/d63334103898471cb0d15ee6027d1abc
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

const ll B = 1000000000; // 1e9 -> 1e9 * 1e9 <= LLONG_MAX (9 * 1e18)
pair<ll, ll> LLONG_MX = pair<ll, ll>(LLONG_MAX / B, LLONG_MAX % B);

int convert(char x){
    if(x <= '9')return x - 48;
    return x - 'a' + 10;
}

ll  convert(const string &s, int base) {
    ll hi = 0, lo = 0;
    for(auto &i: s){
        ll cur = convert(i);
        if(cur >= base)return -1;
        hi = hi * base;
        lo = lo * base;
        lo += cur;
        hi += lo / B;
        lo %= B;
        if(hi * LLONG_MX.second > lo * LLONG_MX.first) return -1;
    }
    return hi * B + lo;
}
vector<tuple<ll, ll, ll>> v;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string a, b; cin >> a >> b;
    for(int i=2;i<=36;i++){
        for(int j=2;j<=36;j++){
            if(i == j)continue;
            ll L = convert(a, i), R = convert(b, j);
            if(!~L || !~R)continue;
            if(L == R) v.emplace_back(L, i, j);
        }
    }
    
    if(v.empty()) {
        cout << "Impossible";
    }
    else if((int)v.size() == 1){
        auto [a, b, c] = v[0];
        cout << a << ' ' << b << ' ' << c;
    }
    else {
        cout << "Multiple";
    }

    return 0;
}
