// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/6fabfcca5d6b483c9f24b81bfabf2124
#include<bits/stdc++.h>

using namespace std;

int arr[105], tmp[105];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=1;i<=N;i++) arr[i] = i; 

    while(N != 1) {
        int idx = 1;
        for(int i=2;i<=N;i+=2) tmp[idx++] = arr[i];
        N = idx - 1;
        for(int i=1;i<=N;i++) arr[i] = tmp[i];
    }
    cout << arr[1];

    return 0;
}
