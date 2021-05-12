// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/542de8e26b06406182f52af66cda1fc8
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s; cin >> s;
    const string DB = "quack";
    int n = s.size();
    vector<int> used(n), cnt(n);
    bool result = true;
    for(int i=0;i<n;i++){
        if(s[i] != 'q')continue;
        int R = i, idx = 0;
        while(idx < 5 && R < n){
            if(used[R] == 0 && s[R] == DB[idx]){
                used[R] = 1;
                idx++;
            }
            R++;
        }
        if(idx != 5) result = false;
        for(int j=i;j<R;j++) cnt[j]++;
    }
    int ans = 0;
    for(int i=0;i<n;i++){
        ans = max(ans, cnt[i]);
        if(cnt[i] == 0)result = false;
    }
    
    if(result)cout << ans;
    else cout << -1;
    return 0;
}
