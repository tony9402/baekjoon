// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/320c53a7494341c0b867034b59ec4377
#include<bits/stdc++.h>

using namespace std;

vector<int> preorder, inorder;
void solve(int L, int R, int L2, int R2) {
    if(L > R || L2 > R2) return;
    int root = preorder[L];
    int idx  = L2;
    while(inorder[idx] != root) idx ++;
    solve(L + 1, L + idx - L2, L2, idx - 1);
    solve(L + idx - L2 + 1, R, idx + 1, R2);
    cout << root << ' ';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        preorder.clear(); preorder.resize(n);
        inorder.clear(); inorder.resize(n);
        for(int i=0;i<n;i++) cin >> preorder[i];
        for(int i=0;i<n;i++) cin >> inorder[i];
        solve(0, n - 1, 0, n - 1);
        cout << '\n';
    }

    return 0;
}
