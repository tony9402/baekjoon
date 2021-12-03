//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/c87761df97d34c1fb97bc85ae388d5e1

#include <bits/stdc++.h>

using namespace std;
vector<int> rope;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N;
    cin >> N;
    for(int i = 0;i < N;i++) {
        int r;
        cin >> r;
        rope.push_back(r);
    }
    
    //오름차순 정렬
    sort(rope.begin(), rope.end());
    
    //가장 가벼운 물건을 들 수 있는 줄 * N개
    //그다음 가벼운 물건을 들 수 있는 줄 * N -1개
    //이런식으로 가장 많이 들 수 있는 경우를 찾는다.
    int weight = rope[0] * N;
    for(int i = 1;i < N;i++){
        if(rope[i] * (N - i) > weight)
            weight = rope[i] * (N - i);
    }

    cout << weight;

    return 0;
} 
