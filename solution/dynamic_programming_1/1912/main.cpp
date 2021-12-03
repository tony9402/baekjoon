//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/1c40c484bfd74219962596b90c8162ea

#include <bits/stdc++.h>

using namespace std;

int arr[100010];
int dp[100010];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int n;
    cin >> n;
    for(int i = 0;i < n;i++)
        cin >> arr[i];

    int _max = arr[0];
    dp[0] = arr[0];

    //dp[i]는 i번째까지 오면서 가질 수 있는 가장 큰 값
    for(int i = 1;i < n;i++){
        dp[i] = max(dp[i - 1] + arr[i], arr[i]);
        _max = max(dp[i],_max);
    }
    cout << _max;

    return 0;
} 
