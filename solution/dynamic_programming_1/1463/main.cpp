// Authored by : tallua_y
// Co-authored by : -
// Link : http://boj.kr/96a171e5da7746c7a51d5d348bc759a8
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    size_t N;
    cin >> N;

    vector<int> count(N + 1);
    count[1] = 0;

    for(int i = 2; i < N + 1; ++i) {
        count[i] = count[i - 1] + 1;
        if (i % 2 == 0) {
            count[i] = min(count[i], count[i / 2] + 1);
        }
        if (i % 3 == 0) {
            count[i] = min(count[i], count[i / 3] + 1);
        }
    }

    cout << count[N] << '\n';

    return 0;
}
