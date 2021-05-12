// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/0351fb8839dd449cbdc10b9e78c47410
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    ll sum = 0, square_sum = 0;
    for(int i=0;i<N;i++) {
        ll x; cin >> x;
        sum += x;
        square_sum += x * x;
    }
    cout << (sum * sum - square_sum) / 2;

    return 0;
}
