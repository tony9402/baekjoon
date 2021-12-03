//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/afdcb0fd1ed64b09b52ef23b966e9bcd

#include <bits/stdc++.h>

using namespace std;

//일을 더 할수있는지 확인하는 함수
//현재 피로도에 A를 더해서 임계점을 넘지않는지 확인
bool can_work(int A, int tired, int M){
    if(tired + A <= M) return true;
    else return false;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int A, B, C, M;  
    cin >> A >> B >> C >> M;

    //24시간동안 일을 진행
    //can_work가 true를 반환하면 일을 한다.
    //false 반환시 쉬어서 피로도를 줄인다.
    int time = 24, tired = 0, work = 0;
    while(time--){
        if(can_work(A, tired, M)){
            work += B;
            tired += A;
        }
        else{
            tired -= C;
            if(tired < 0) tired = 0;
        }
    }
    cout << work;

    return 0;
} 
