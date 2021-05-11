// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/dc356e3adafd4e158b47dce9a9acd59b
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    int answer = 0;
    vector<int> V(N);
    for(int i=0;i<N;i++) cin >> V[i];
    for(int i=0;i<N;i++) {
        for(int j=i+1;j<N;j++) {
            for(int k=j+1;k<N;k++) {
                int value = V[i] + V[j] + V[k];
                if(value > M) continue;
                answer = max(answer, value);
            }
        }
    }
    cout << answer;

    return 0;
}
