// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/67eb3ee9ba7649f29c3542bb2b034e08
#include<bits/stdc++.h>

using namespace std;

int arr[222][222];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            cin >> arr[i][j];
            arr[i][j] += arr[i-1][j];
        }
    }

    int answer = INT_MIN;
    for(int i=1;i<=N;i++){
        for(int j=i;j<=N;j++) {
            int sum = 0;
            for(int k=1;k<=M;k++){
                int cur = arr[j][k] - arr[i - 1][k];
                sum += cur;
                if(sum < cur) sum = cur;
                answer = max(answer, sum);
            }
        }
    }
    cout << answer;

    return 0;
}
