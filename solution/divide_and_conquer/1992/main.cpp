// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/f4a1319fd1af4655b19f5c7cd7872b92
#include<bits/stdc++.h>

using namespace std;

char arr[66][66];
string answer;

void solve(int y, int x, int s) {
    bool flag = true;
    for(int i=0;i<s;i++) {
        for(int j=0;j<s;j++) {
            if(arr[y][x] != arr[y + i][x + j])flag = false;
        }
    }
    if(flag) answer += arr[y][x];
    else  {
        s /= 2;
        answer += "(";
        solve(y    , x    , s);
        solve(y    , x + s, s);
        solve(y + s, x    , s);
        solve(y + s, x + s, s);
        answer += ")";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++) cin >> arr[i];
    solve(0, 0, N);
    cout << answer;

    return 0;
}
