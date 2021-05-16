// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/5aee7052f3ee45d5b0294edfb54c92f1
#include<bits/stdc++.h>

using namespace std;

string answer;

void dfs(int L, int dis) {
    if(dis == 1) {
        answer[L] = '-';
        return;
    }

    dis /= 3;
    dfs(L, dis);
    dfs(L + 2 * dis, dis);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int k;
    while(cin >> k) {
        int N = 1;
        for(int i = 0; i < k; i++) N *= 3;
        answer = string(N, ' ');
        dfs(0, N);
        cout << answer << '\n';
    }

    return 0;
}

