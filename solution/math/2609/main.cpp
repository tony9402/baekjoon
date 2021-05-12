// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/054bab418a2c441a99982acfa1ba2b27
#include<bits/stdc++.h>

using namespace std;

int gcd(int a, int b) {
    if(b == 0)return a;
    return gcd(b, a % b);
}
int lcm(int a, int b){
    return a / gcd(a, b) * b;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int a, b; cin >> a >> b;
    cout << gcd(a, b) << '\n' << lcm(a, b);

    return 0;
}
