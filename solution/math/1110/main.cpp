// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/29790baf467142729acef15a2815b478
#include<bits/stdc++.h>

using namespace std;

int getNext(int x) {
    int tmp = x, ret = 0;
    while(x) {
        ret += x % 10;
        x /= 10;
    }
    return tmp % 10 * 10 + ret % 10;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    int start = N;
    int cur   = start;
    int ans = 0;

    while(true) {
        cur = getNext(cur);
        ans ++;
        if(start == cur) break;
    }
    cout << ans;

    return 0;
}
