// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/19379bdb38884854badc892db21a8d6b
#include<bits/stdc++.h>

using namespace std;

int cal(int x) {
    int tmp = x;
    while(x) {
        tmp += x % 10;
        x /= 10;
    }
    return tmp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    int cur = 1;
    while(cur < N + 100 && N != cal(cur)) cur++;
    if(cur == N + 100) cur = 0;
    cout << cur;

    return 0;
}
