// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/3e340e082d68472b8a8559566398507e
#include<bits/stdc++.h>

using namespace std;

int arr[1005][1005], prefix[1005][2];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    int total = 0, answer = 0;
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            int &x = arr[i][j];
            cin >> x;
            if(1 < j && j < M) x <<= 1;
            if(1 < i && i < N) x <<= 1;
            total += x;
            prefix[i][0] += x;
            prefix[j][1] += x;
        }
    }
    answer = total;

    for(int i=2;i<N;i++) {
        answer = max(answer, total - prefix[i][0] / 2 + prefix[1][0]);
        answer = max(answer, total - prefix[i][0] / 2 + prefix[N][0]);
    }
    for(int j=2;j<M;j++) {
        answer = max(answer, total - prefix[j][1] / 2 + prefix[1][1]);
        answer = max(answer, total - prefix[j][1] / 2 + prefix[M][1]);
    }
    cout << answer;

    return 0;
}
