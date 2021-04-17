#include<bits/stdc++.h>

using namespace std;

int arr[33][33];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=0;i<N;i++) for(int j=0;j<M;j++) cin >> arr[i][j];
    int answer = 0;
    for(int i=0;i<M;i++){
        for(int j=i+1;j<M;j++){
            for(int k=j+1;k<M;k++){
                int cur = 0;
                for(int l=0;l<N;l++) {
                    cur += max({ arr[l][i], arr[l][j], arr[l][k] });
                }
                answer = max(answer, cur);
            }
        }
    }
    cout << answer;

    return 0;
}
