// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a1f005e8ee00409590b55623b8057ff0
#include<bits/stdc++.h>

using namespace std;

bool chk(int a, int b) {
    for(int i=0;i<2;i++) {
        if(a % 10 == b) return true;
        a /= 10;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K; cin >> N >> K;
    int answer = 0;
    for(int i=0;i<(N+1)*3600;i++) {
        int hh = i / 3600;
        int mm = i / 60 % 60;
        int ss = i % 60;
        if(chk(hh, K) || chk(mm, K) || chk(ss, K)) answer++;
    }
    cout << answer;

    return 0;
}
