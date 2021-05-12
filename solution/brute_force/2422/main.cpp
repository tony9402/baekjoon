// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/514a7a75b2eb4a2eaf862e8227682be7
#include<bits/stdc++.h>

using namespace std;

bool chk[222][222];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M; cin >> N >> M;
    for(int i=0;i<M;i++) {
        int a, b; cin >> a >> b;
        chk[a][b] = chk[b][a] = true;
    }
    int answer = 0;
    for(int i=1;i<=N;i++) {
        for(int j=i+1;j<=N;j++) {
            for(int k=j+1;k<=N;k++) {
                if(chk[i][j] || chk[j][k] || chk[i][k])continue;
                answer++;
            }
        }
    }
    cout << answer;

    return 0;
}
