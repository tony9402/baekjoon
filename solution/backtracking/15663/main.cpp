// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/07e0a7b8b518418d86ac107dcdf56a7e
#include<bits/stdc++.h>

using namespace std;

int arr[10], choose[10], N, M;
bool used[10];

void dfs(int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << arr[choose[i]] << ' ';
        }
        cout << '\n';
        return;
    }
    int pre = -1;
    for(int i=0;i<N;i++) {
        if(used[i] || pre == arr[i]) continue;
        pre = arr[i];
        used[i] = true;
        choose[cnt] = i;
        dfs(cnt + 1);
        used[i] = false;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for(int i=0;i<N;i++) cin >> arr[i];
    sort(arr, arr + N);
    dfs(0);

    return 0;
}
