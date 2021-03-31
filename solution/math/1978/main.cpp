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

    int n; cin >> n;
    int answer = 0;
    for(int i=0;i<n;i++){
        int x; cin >> x;
        if(isPrime(x)) answer ++;
    }
    cout << answer;

    return 0;
}
