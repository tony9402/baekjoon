// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/76369f4f8225439084adb5f553cecae8
#include<bits/stdc++.h>

using namespace std;

vector<string> file;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    for(int i=0;i<n;i++){
        string s; cin >> s;
        file.emplace_back(s.substr(s.find(".") + 1));
    }
    sort(file.begin(), file.end());
    for(int i=0;i<n;){
        int j=i+1, cnt=1;
        while(j<n && file[i]==file[j])j++, cnt++;
        cout << file[i] << ' ' << cnt << '\n';
        i = j;
    }

    return 0;
}
