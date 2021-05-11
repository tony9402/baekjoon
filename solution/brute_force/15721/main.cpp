// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/2e1ee57b7481444fad22d74a53c6ac21
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int A, T, B; cin >> A >> T >> B;
    int answer = -1;
    for(int i=1; T ;i++){
        for(int j=0;T && j<4;j++) {
            T -= (j % 2 == B);
            ++answer;
        }
        for(int j=0;T && j<2;j++) {
            for(int k=0;T && k<=i;k++) {
                T -= (j % 2 == B);
                ++answer;
            }
        }
    }
    cout << answer % A;

    return 0;
}
