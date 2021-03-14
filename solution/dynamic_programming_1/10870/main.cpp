#include <iostream>

using namespace std;

int DP[25];

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    // index -> 0  1  2  3  4  5  6  7 
    // value -> 0  1  1  2  3  5  8 13 
    
    // DP[0] = 0
    // DP[1] = 1
    // DP[i] = DP[i - 1] + DP[i - 2] (i ≥ 2)

    DP[0] = 0; //전역으로 DP 배열 선언 했으므로, 0으로 초기화 되므로 이 라인 지워도 됨.
    DP[1] = 1;
    for(int i=2;i<=20;i++){
        DP[i] = DP[i - 1] + DP[i - 2];
    }

    int N; cin >> N;
    cout << DP[N];
}
