// Authored by : tallua
// Co-authored by : -
// Link : http://boj.kr/529bea24f4ef45f3a65713bab79f6b3f

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> count(N + 1);
    count[1] = 0;

    for(size_t i = 2; i < N + 1; ++i) {
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