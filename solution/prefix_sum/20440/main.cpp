// Authored by : tony9402
// Co-authored by : -
// Link : http://boj.kr/ded80dcd2d094ee8af7c04ff371b3749
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<pair<int, int>> V;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0;i<N;i++) {
        int s, e; cin >> s >> e;
        V.emplace_back(s, +1);
        V.emplace_back(e, -1);
    }
    sort(V.begin(),V.end());
    int ansL = -1, ansR = -1;
    int sum = 0, mx = 0;
    for(int i=0;i<2 * N;i++) {
        sum += V[i].second;
        mx = max(mx, sum);
    }

    for(int i=0;i<2 * N;i++) {
        sum += V[i].second;
        if(i + 1 < 2 * N && V[i + 1].first == V[i].first) continue;
        if(!~ansL) {
            if(sum == mx) {
                ansL = V[i].first;
            }
        }
        else if(sum != mx) {
            ansR = V[i].first;
            break;
        }
    }
    cout << mx << '\n';
    cout << ansL << " " << ansR;

    return 0;
}
