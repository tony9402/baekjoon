#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    // x_1 x_2 + x_2 x_3 + x_3 x_4 + ... x_n-1 x_n => O(N^2)
    // = { (x_1 + x_2 + x_3 ... + x_n) ^ 2 - (x_1 ^ 2 + x_2 ^ 2 + x_3 ^ 2 + ... + x_n ^ 2) } / 2 => O(N)

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
