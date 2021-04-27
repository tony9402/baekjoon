#include<bits/stdc++.h>

using namespace std;

int prefix[1030][1030];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q; cin >> N >> Q;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=N;j++) {
            cin >> prefix[i][j];
            prefix[i][j] = prefix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1];
        }
    }

    while(Q--){
        int a, b, c, d; cin >> a >> b>> c>>d;
        a--; b--;
        cout << prefix[c][d] - prefix[a][d] - prefix[c][b] + prefix[a][b] << '\n';
    }

    return 0;
}
