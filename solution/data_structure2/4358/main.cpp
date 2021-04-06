#include<bits/stdc++.h>

using namespace std;

// 순서가 중요하니 unordered_map 말고 map
map<string, int> mp;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s;
    int total = 0;
    while(getline(cin, s)) {
        mp[s] += 1; // mp에 없는 경우 0으로 생성 후 +1
        total += 1;
    }

    // 소수점 4째자리까지
    cout.precision(4);
    cout << fixed;
    for(auto &[k, v]: mp) {
        cout << k << ' ' << v * 100.0 / total << '\n';
    }

    return 0;
}
