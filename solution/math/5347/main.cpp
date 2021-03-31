#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

ll gcd(ll a, ll b){
    return b ? gcd(b, a % b) : a;
}
ll lcm(ll a, ll b) {
    return a / gcd(a, b) * b;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        ll a, b; cin >> a >> b;
        cout << lcm(a, b) << '\n';
    }

    return 0;
}
