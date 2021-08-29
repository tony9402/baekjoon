// Authored by : tallua_y
// Co-authored by :
// Link : http://boj.kr/9efb426713394b95921f674b0ac0f735
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // map<begin point, end point>
    map<int, int> circles;

    size_t N;
    cin >> N;

    bool is_valid = true;
    while (N--) {
        int x, r;
        cin >> x >> r;

        const int begin = x - r;
        const int end = x + r;

        // circle started same is not valid
        const auto circle_after = circles.lower_bound(begin);
        if (circle_after != circles.end() && circle_after->first == begin) {
            is_valid = false;
            break;
        }

        // circle started after should stop before this circle
        if (circle_after != circles.end() && circle_after->first <= end && end <= circle_after->second) {
            is_valid = false;
            break;
        }

        // circle started before should stop after this circle
        const auto circle_begin = circle_after != circles.begin() ? std::prev(circle_after) : circles.end();
        if (circle_begin != circles.end() && circle_begin->second <= end && begin <= circle_begin->second) {
            is_valid = false;
            break;
        }

        // add circle
        circles.insert({begin, end});
    }

    if (is_valid) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
