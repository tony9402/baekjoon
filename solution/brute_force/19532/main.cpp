// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/605780919d644059a745b5ae43d221be
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int> V(6);
    for(int i=0;i<6;i++) cin >> V[i];

    for(int x = -1000; x <= 1000; x++) {
        for(int y = -1000; y <= 1000; y++) {
            int F = V[0] * x + V[1] * y - V[2];
            int S = V[3] * x + V[4] * y - V[5];
            if(F == 0 && S == 0) {
                cout << x << ' ' << y;
                return 0;
            }
        }
    }

    return 0;
}
