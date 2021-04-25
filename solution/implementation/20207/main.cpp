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
