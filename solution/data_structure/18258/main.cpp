// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/9bc206242acc4800a1f1df61d2b1b062
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    queue<int> Q;
    while(T--) {
        string cmd; cin >> cmd;
        if(cmd == "push") {
            int X; cin >> X;
            Q.push(X);
        }
        else if(cmd == "pop") {
            if(Q.empty()) cout << -1 << '\n';
            else {
                cout << Q.front() << '\n';
                Q.pop();
            }
        }
        else if(cmd == "size") {
            cout << (int)Q.size() << '\n';
        }
        else if(cmd == "empty") {
            cout << Q.empty() << '\n';
        }
        else if(cmd == "front") {
            if(Q.empty()) cout << -1 << '\n';
            else cout << Q.front() << '\n';
        }
        else if(cmd == "back") {
            if(Q.empty()) cout << -1 << '\n';
            else cout << Q.back() << '\n';
        }
    }

    return 0;
}
