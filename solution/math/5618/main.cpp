// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/1df904530afc47edbe9a9983b130ce19
#include<bits/stdc++.h>

using namespace std;

int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b, a%b);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    int a, b; cin >> a >> b;
    a = gcd(a, b);
    if(n == 3) {
        int c; cin >> c;
        a = gcd(a, c);
    }

    vector<int> ans;
    for(int i=1;i*i<=a;i++){
        if(a % i != 0) continue;
        ans.push_back(i);
        if(i * i != a) ans.push_back(a / i);
    }
    sort(ans.begin(), ans.end());
    for(int i=0;i<(int)ans.size();i++){
        cout << ans[i] << '\n';
    }

    return 0;
}
