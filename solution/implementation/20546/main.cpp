// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/a30111114ee042f983774cf658e84fb9
#include<bits/stdc++.h>

using namespace std;

int info[14];

int MachineJ(int money){
    int cnt = 0;
    for(int i=0;i<14;i++){
        if(info[i] > money) continue;
        cnt = money / info[i];
        money %= info[i];
    }
    return money + cnt * info[13];
}

int MachineS(int money){
    int cnt = 0;
    int downCnt = 0;
    int upCnt = 0;
    for(int i=1;i<14;i++){
        if(info[i-1] > info[i]){
            downCnt ++;
            upCnt = 0;
        }
        else if(info[i-1] < info[i]){
            downCnt = 0;
            upCnt++;
        }
        else downCnt = upCnt = 0;

        if(info[i] <= money && downCnt >= 3){
            cnt += money / info[i];
            money %= info[i];
        }
    }
    return money + cnt * info[13];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int money; cin >> money;
    for(int i=0;i<14;i++) cin >> info[i];
    
    int BNP = MachineJ(money);
    int TIMING = MachineS(money);

    if(BNP > TIMING)cout << "BNP";
    else if(BNP < TIMING)cout << "TIMING";
    else cout << "SAMESAME";

    return 0;
}
