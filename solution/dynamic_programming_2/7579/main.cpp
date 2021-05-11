// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/7cc3cfd9bda64cfe8af9ff0a99c789a9
#include<bits/stdc++.h>

using namespace std;

int DP[10001], N, M, mem[101], cost[101];
int sum_cost;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for(int i=0;i<N;i++) cin >> mem[i];
    for(int i=0;i<N;i++) {
        cin >> cost[i];
        sum_cost += cost[i];
    }
    for(int i=0;i<N;i++) {
        for(int j=sum_cost;j>=0;j--){
            if(j - cost[i] >= 0){
                DP[j] = max(DP[j], DP[j - cost[i]] + mem[i]);
            }
        }
    }
    int answer = 0;
    for(int i=0;i<=sum_cost;i++) {
        if(DP[i] >= M) {
            answer = i;
            break;
        }
    }
    cout << answer;

    return 0;
}
