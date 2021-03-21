#include<bits/stdc++.h>

using namespace std;

int used[105];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    // 초기화
    for(int i=0;i<=100;i++) used[i] = -1;

    int n; cin >> n;
    int answer = 0;
    for(int i=0;i<n;i++){
        int num, loc; cin >> num >> loc;

        if(used[num] < 0) used[num] = loc;
        else if(used[num] != loc){
            used[num] = loc;
            answer ++;
        }
    }
    cout << answer;

    return 0;
}
