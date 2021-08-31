// Authored by : dart
// Co-authored by : -
// Link : http://boj.kr/50c45e2707d946d98571bbeb52348d60
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
string word;
int red = 0, blue = 0;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> word;

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            if (word[i] == 'B') { blue++; }
            if (word[i] == 'R') { red++; }
        }
        else {
            if (word[i] == 'B' && word[i - 1] == 'R') { blue++; }
            if (word[i] == 'R' && word[i - 1] == 'B') { red++; }
        }
    }
    cout << min(red, blue) + 1 << "\n";


    return 0;
}