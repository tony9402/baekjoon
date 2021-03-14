#include<iostream>
#include<algorithm>

using namespace std;

int DP[5005];

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    // DP[i] : i kg 배달을 할때 봉지의 최소 개수
    // DP[i] = min(DP[i], DP[i - 3] + 1) (i ≥ 3)
    // DP[i] = min({DP[i], DP[i - 3] + 1, DP[i - 5] + 1})  (i ≥ 5)
    // 0, 1, 2일때 초기화를 해놓자.
    // 
    // 0은 아무것도 안가져가는 경우( 0 )이 존재하므로 DP[0] = 0
    // 1, 2 은 가능한 경우가 없음 -> DP[1] = DP[2] = INF 
    // (INF 는 DP 값으로 올 수 있는 경우보다 큰 값으로 초기화 해야함)
    // 또한 i ≥ 3인 경우는 아직 최솟값을 뽑기 전이라 INF로 초기화 해야함
    //
    // 초기화 정리
    // DP[i] 
    // i == 0, DP[i] = 0
    // i ≥ 1,  DP[i] = INF
    
    const int INF = 50000;
    for(int i=1;i<=5000;i++) DP[i] = INF;
    DP[3] = 1; 
    //DP[4] = INF; 4인 경우는 불가능 함
    for(int i=5;i<=5000;i++) DP[i] = min({ DP[i], DP[i - 3] + 1, DP[i - 5] + 1});
        
    // 만약 DP가 INF면 -1 출력 아니면 DP[i] 출력
    int N; cin >> N;
    if(DP[N] == INF)DP[N] = -1;
    cout << DP[N];
}
