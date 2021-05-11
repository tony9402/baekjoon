// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/3955b249d38d4c79851d4cf97d474c0b
#include<bits/stdc++.h>

using namespace std;

int choose[10];
int arr[10], N, M;
bool used[10];

void dfs(int cnt) {
    if(cnt == M) {
        for(int i=0;i<M;i++) {
            cout << arr[choose[i]] << '\n';
        }
        return;
    }

    for(int i=0;i<N;i++){
        if(used[i]) continue;
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
