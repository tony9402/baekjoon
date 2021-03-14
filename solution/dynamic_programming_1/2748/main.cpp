#include<iostream>

using namespace std;

long long DP[99];

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    // 계산 과정에서 int 범위를 벗어나는게 있음.
    // DP 식은 boj.kr/10870 와 동일
    
    DP[1] = 1;
    for(int i=2;i<=90;i++)DP[i] = DP[i-1] + DP[i-2];
    
    int N; cin >> N;
    cout << DP[N];
}

