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
