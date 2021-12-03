//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/601b9a43e4c34576a027eb34f7360f63

#include <bits/stdc++.h>

using namespace std;

string bignumAdd(string num1, string num2);
string dp[110][110];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;

    //큰수 조합 문제입니다. long long형도 벗어나기 때문에
    //string으로 입력받아 계산을 진행합니다.
    //조합은 dp문제로 풀이합니다.(파스칼의 삼각형)
    dp[0][0] = "1";
    for(int i = 1;i <= n;i++){
        dp[i][0] = "1";
        for(int j = 1;j <= i;j++)
            dp[i][j] = bignumAdd(dp[i - 1][j - 1], dp[i - 1][j]);
    }

    cout << dp[n][m];

    return 0;
} 

string bignumAdd(string num1, string num2){
    string result = "";
    int plus = 0;
    //plus는 자리 올림을 담당합니다.
    //1의자리부터 올라가며 더합니다.
    while(!num1.empty() || !num2.empty() || plus){
        if(!num1.empty()){
            plus += num1.back() - '0';
            num1.pop_back();
        }
        if(!num2.empty()){
            plus += num2.back() - '0';
            num2.pop_back();
        }
        result += (plus % 10) + '0';
        plus /= 10;
    }

    reverse(result.begin(), result.end());
    return result;
}
