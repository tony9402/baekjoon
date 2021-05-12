// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/3aaead48f31d48d19a9884356908d293
#include<bits/stdc++.h>

using namespace std;

int arr[100005], prefix[100005];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=1;i<=N;i++) cin >> arr[i];
    for(int i=1;i<=N;i++) {
        if(arr[i] > arr[i + 1]) prefix[i] = 1;
        prefix[i] += prefix[i - 1];
    }

    int Q; cin >> Q;
    while(Q--){
        int x, y; cin >> x >> y;
        --x; --y;
        cout << prefix[y] - prefix[x] << '\n';
    }

    return 0;
}
