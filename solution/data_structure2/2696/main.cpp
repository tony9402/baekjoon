// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/c5acf6a6a2f24b4ca0c415fbe1947571
#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        priority_queue<int> L;
        priority_queue<int, vector<int>, greater<int>> R;
        vector<int> answer;
        for(int i=0;i<n;i++) {
            int x; cin >> x;
            R.push(x);

            while(L.size() < R.size()) {
                L.push(R.top());
                R.pop();
            }
            while(L.size() > R.size() + 1) {
                R.push(L.top());
                L.pop();
            }
            while(!L.empty() || !R.empty()) {
                int valueL = L.top();
                int valueR = R.top();
                if(valueL <= valueR) break;
                L.pop();
                R.pop();
                L.push(valueR);
                R.push(valueL);
            }
            
            if(i % 2 == 0) answer.push_back(L.top());
        }
        cout << answer.size() << '\n';
        for(int i=0;i<(int)answer.size();i++) {
            cout << answer[i];
            if(i + 1 != (int)answer.size() && (i + 1) % 10 == 0) cout << '\n';
            else cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
