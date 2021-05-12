// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/67887b7c21504d718bfffa859b209589
#include<bits/stdc++.h>

using namespace std;

char stars[444][444];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    int N = 4 * (n - 1) + 1;
    for(int k=0;k<=N/2;k+=2){
        int L = N - k * 2;
        for(int i=0;i<L;i++){
            stars[k + i][k] = stars[k][k + i] = stars[k + L - 1][k + i] = stars[k + i][k + L - 1] = '*';
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(stars[i][j] == '*')cout << '*';
            else cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
