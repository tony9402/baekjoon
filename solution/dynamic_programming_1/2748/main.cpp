// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/b5fdc8a3c2c84784a6b308c98e4aa7e9
#include<bits/stdc++.h>

using namespace std;

long long DP[99];

int main(){
    ios::sync_with_stdio(false); 
    cin.tie(0);

    DP[1] = 1;
    for(int i=2;i<=90;i++)DP[i] = DP[i-1] + DP[i-2];
    
    int N; cin >> N;
    cout << DP[N];
}

