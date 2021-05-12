// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/bf53232ebf90497bbcdea9716eade1e8
#include<bits/stdc++.h>

using namespace std;

bool erased[1005];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int K, N; cin >> N >> K;
    for(int i=2;K && i<=N;i++){
        if(erased[i])continue;
        for(int j=i;K && j<=N;j+=i){
            if(erased[j])continue;
            erased[j] = true;
            if(--K == 0) cout << j;
        }
    }

    return 0;
}
