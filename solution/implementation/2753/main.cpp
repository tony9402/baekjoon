// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a5fabcbae0604daabb17802f9323c69f
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    if(n % 4 == 0 && (n % 100 != 0 || n % 400 == 0)){
        cout << 1;
    }
    else {
        cout << 0;
    }

    return 0;
}
