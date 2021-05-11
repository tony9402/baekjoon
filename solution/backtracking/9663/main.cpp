// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/bb3cca54213d47268ddc82a82728f730
#include<bits/stdc++.h>

using namespace std;

int n, ans;
bool Y[22], DL[44], DR[44];

void dfs(int y, int cnt){
    if(cnt == n){
        ans++; 
        return;
    }
    for(int j=0;j<n;j++){
        if(Y[j] || DL[y + j] || DR[y - j + n])continue;
        Y[j] = DL[y + j] = DR[y - j + n] = true;
        dfs(y + 1, cnt + 1);
        Y[j] = DL[y + j] = DR[y - j + n] = false;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    dfs(0, 0);
    cout << ans;

    return 0;
}
