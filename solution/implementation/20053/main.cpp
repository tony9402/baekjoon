#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int max_value = -1'000'001, min_value = 1'000'001;
        for(int i=0;i<n;i++){
            int x; cin >> x;
            if(max_value < x) max_value = x;
            if(min_value > x) min_value = x;
        }
        cout << min_value << ' '  << max_value << '\n';
    }

    return 0;
}

