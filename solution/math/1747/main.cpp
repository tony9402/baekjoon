// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/b94e3339437045b3adbc71d22ec88114
#include<bits/stdc++.h>

using namespace std;

bool isPrime(int x) {
    if(x <= 1) return false;
    for(int i=2;i*i<=x;i++){
        if(x % i == 0) return false;
    }
    return true;
}

bool isPalindrome(int x) {
    int origin = x;
    int rev    = 0;
    while(x) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return origin == rev;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    while(true) {
        if(isPalindrome(n) && isPrime(n)) break;
        n ++;
    }
    cout << n;

    return 0;
}
