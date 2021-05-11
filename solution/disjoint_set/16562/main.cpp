// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/caef773ebb994d6e854c390d5fe22057
#include<bits/stdc++.h>

using namespace std;

int uf[10101], arr[10101];

int find(int x) {
    if(uf[x] < 0) return x;
    return uf[x] = find(uf[x]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if(a == b) return false;
    uf[b] = a;
    arr[a] = min(arr[a], arr[b]);
    arr[b] = 0;
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, k; cin >> n >> m >> k;
    for(int i=1;i<=n;i++) {
        uf[i] = -1;
        cin >> arr[i];
    }
    for(int i=0;i<m;i++) {
        int a, b; cin >> a >> b;
        merge(a, b);
    }
    int answer = 0;
    for(int i=1;i<=n;i++) answer += arr[i];
    if(answer > k) cout << "Oh no";
    else cout << answer;

    return 0;
}
