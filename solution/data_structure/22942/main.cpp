// Authored by : tallua_y
// Co-authored by :
// Link : http://boj.kr/7637094ad3f24a62939ad2b4811c9f77
#include <bits/stdc++.h>

using namespace std;

struct circle_t {
    int begin;
    int end;
};

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    size_t N;
    cin >> N;

    vector<circle_t> circles(N);
    while (N--) {
        int x, r;
        cin >> x >> r;

        const int begin = x - r;
        const int end = x + r;

        circles[N] = {begin, end};
    }

    sort(circles.begin(), circles.end(), [](circle_t const& lhs, circle_t const& rhs) {
        return lhs.begin != rhs.begin ? lhs.begin < rhs.begin : lhs.end < rhs.end;
    });

    bool is_valid = true;
    vector<decltype(circle_t::end)> end_stack;
    for (auto const& circle : circles) {
        // prune circle not ended
        while (!end_stack.empty() && end_stack.back() < circle.begin) {
            end_stack.pop_back();
        }

        // circle should not exist between other circle
        if (!end_stack.empty() && circle.begin <= end_stack.back() && end_stack.back() <= circle.end) {
            is_valid = false;
            break;
        }

        end_stack.push_back(circle.end);
    }

    if (is_valid) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
