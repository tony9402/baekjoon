#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

bool isPrime(ll x) {
    if(x < 2) return false;
    for(ll i=2;i*i<=x;i++){
        if(x % i == 0) return false;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int t; cin >> t;
    while(t--){
        ll x; cin >> x;
        while(!isPrime(x))x++;
        cout << x << '\n';
    }

    return 0;
}
