//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/4f5289fb7dfb4ef98d88be1ba54438ea

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    
    int N;
    cin >> N;

    //짝수일때는 창영이가, 홀수일때는 상근이가 이기게 됩니다.
    //상근이가 먼저 시작하고 반드시 1개 또는 3개(홀수개)를 가져가기 떄문
    cout << ((N % 2 == 0) ? "CY" : "SK");

    return 0;
} 
