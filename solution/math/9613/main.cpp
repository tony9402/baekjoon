// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/81fae9eae6b04d77bb40a1d3fb340b3c
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int gcd(int a, int b){
    if(b == 0)return a;
    return gcd(b, a % b);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        int n;cin >> n;
        vector<int> v(n);
        for(int i=0;i<n;i++)cin >> v[i];
        ll ans = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                ans += gcd(v[i], v[j]);
            }
        }
        cout << ans << '\n';
    }

    return 0;
}
