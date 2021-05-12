// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/f3c6407dc6ab4ad38ebb74b1ea3a9c8e
#include<bits/stdc++.h>

using namespace std;

bool isPrime(int x) {
    if(x <= 1) return false;
    for(int i=2;i*i<=x;i++) {
        if(x % i == 0) return false;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int sum = 0, minimum = 10001;
    int l, r; cin >> l >> r;
    for(int i=l;i<=r;i++){
        if(isPrime(i)) {
            sum += i;
            minimum = min(minimum, i);
        }
    }
    if(sum) {
        cout << sum << '\n';
        cout << minimum;
    }
    else {
        cout << -1;
    }
    return 0;
}

