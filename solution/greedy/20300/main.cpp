// Authored by : dart
// Co-authored by : -
// Link : http://boj.kr/50c45e2707d946d98571bbeb52348d60
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
ll arr[10005];
ll ans = 0;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    //최대 원소와 최소 원소가 합쳐지는 게 근손실이 최소이다
    if (n % 2 == 0) {
        for (int i = 0; i < n / 2; i++) {
            ans = max(ans, arr[i] + arr[n - i - 1]);
        }
    }
        //홀수일 때는 마지막 하나의 운동기구가 남는다
    else {
        for (int i = 0; i < n / 2; i++) {
            ans = max(ans, arr[i] + arr[n - i - 2]);
        }
        ans = max(ans, arr[n - 1]);
    }
    cout << ans << "\n";


    return 0;
}