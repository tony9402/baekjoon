// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/495000f668564c6c9a71fa59b0380aae
#include<bits/stdc++.h>

using namespace std;
int prefix[444];

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    int n; cin >> n;
    for(int i=1;i<=n;i++){
        int a, b; cin >> a >> b;
        prefix[a]++; prefix[b+1]--;    
    }
    int mx = 0, ans = 0, prv = -1;
    for(int i=1;i<=366;i++){
        prefix[i]+=prefix[i-1];
        mx=max(mx,prefix[i]);
        if(!prefix[i]){
            ans += (i - prv) * mx;
            mx = 0; prv = -1;
        }
        else if(!~prv)prv = i;
    }
    cout << ans;
    
    return 0;
}
