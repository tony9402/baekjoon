// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ba10084d78354aeabad7a57999d07356
#include<bits/stdc++.h>

using namespace std;

int arr[10], choose[10], N, M;

void dfs(int idx, int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << arr[choose[i]] << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i=idx;i<N;i++) {
        choose[cnt] = i;
        dfs(i, cnt + 1);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for(int i=0;i<N;i++) cin >> arr[i];
    sort(arr, arr + N);
    dfs(0, 0);

    return 0;
}
