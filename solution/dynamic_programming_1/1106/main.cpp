//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c4014687c4054e5bbf391269f4b7551b

#include <bits/stdc++.h>

using namespace std;
pair<int, int> city[30];
int dp[100010];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int C, N;
    cin >> C >> N;

    for(int i = 0;i < N;i++){
        int cost, customer;
        cin >> cost >> customer;
        city[i] = make_pair(cost, customer);
    }

    //dp[i]는 i의 비용으로 최대 늘릴 수 있는 고객의 수
    //따라서 각 도시들을 돌면서 늘릴 수 있는 고객의 수를 비교하며
    //dp에 최대값을 저장합니다.
    for(int i = 1;i < 100001;i++){
        for(int j = 0;j < N;j++){
            if(city[j].first <= i)
                dp[i] = max(dp[i], dp[i - city[j].first] + city[j].second);
        }
        //i원일 때 늘릴 최소인원 C를 만족한다면
        //i를 출력합니다.
        if(dp[i] >= C){
            cout << i << '\n';
            break;
        }
    }

    return 0;
}
