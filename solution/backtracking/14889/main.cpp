// Authored by : jybin321
// Co-authored by : -
// Link : http://boj.kr/1352b81ac8c5417f908c5e9fd2f395d9

#include <bits/stdc++.h>
using namespace std;
int n, ans = INT_MAX, arr[21][21];
bool v[21];

void input() {
    cin >> n;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < n; j++) 
            cin >> arr[i][j];
}

int check(int clan) {
    int res = 0;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < n; j++) 
            if(v[i] == clan && v[j] == clan) 
                res += arr[i][j];
    return res;
}

void func(int idx, int cnt) {
    if(idx == n / 2) {
        int a = check(1);
        int b = check(0);
        ans = min(ans, abs(a - b));
        return;
    }

    for(int i = cnt; i < n; i++) {
        if(v[i]) continue;
        v[i] = 1;
        func(idx + 1, i);
        v[i] = 0;
    }
}

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    input();
    func(0, 0);
    cout << ans;
    return 0;
}
