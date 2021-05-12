// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/cb5e9a75972a4ac59cc7b4428d07f2fa
#include<bits/stdc++.h>

using namespace std;

int arr[10], choose[10], N, M;
bool used[10];

void dfs(int idx, int cnt) {
    if(cnt == M){
        for(int i=0;i<M;i++) {
            cout << arr[choose[i]] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i=idx;i<N;i++) {
        if(used[i]) continue;
        used[i] = true;
        choose[cnt] = i;
        dfs(i + 1, cnt + 1);
        used[i] = false;
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
