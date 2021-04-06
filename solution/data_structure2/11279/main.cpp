#include<bits/stdc++.h>

using namespace std;

priority_queue<int> pq;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    pq.push(0);
    for(int i=0;i<N;i++){
        int x;cin >> x;
        if(x == 0) {
            if(pq.empty()) cout << 0 << '\n';
            else { 
                cout << pq.top() << '\n';
                pq.pop();
            }
        }
        else pq.push(x);
    }

    return 0;
}
